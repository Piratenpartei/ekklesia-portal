import re

import requests


def parse_raw_content(raw: str):
    subsection_pattern = '((?:[^#]|#{3,})+)'
    abstract_header = '^## (?:(?:Zusammenfassung)|(?:Abstract))\n+'
    content_header = '^## (?:(?:Proposition)|(?:Antragstext))\n+'
    motivation_header = '^## (?:(?:Motivation)|(?:Begründung))\n+'

    content_match = re.search(content_header + subsection_pattern, raw, re.MULTILINE)
    abstract_match = re.search(abstract_header + subsection_pattern, raw, re.MULTILINE)
    motivation_match = re.search(motivation_header + subsection_pattern, raw, re.MULTILINE)

    if content_match:
        abstract = abstract_match.group(1).strip() if abstract_match else None
        content = content_match.group(1).strip()
        motivation = motivation_match.group(1).strip() if motivation_match else None
    else:
        content = raw
        abstract = None
        motivation = None

    return {
        'abstract': abstract,
        'content': content,
        'motivation': motivation,
        'all_matched': content and abstract and motivation
    }


def import_discourse_post_as_proposition(config: dict, from_data):
    base_url = config["base_url"]
    post_id = int(from_data)
    post_url = f"{base_url}/posts/{post_id}"

    headers = {'accept': 'application/json'}
    if  "api_key" in config:
        headers['api-key'] = config["api_key"]
        headers['api-username'] = config["api_username"]

    res = requests.get(post_url, headers=headers)
    post_data = res.json()

    raw = post_data.get("raw")
    if raw is None:
        raise ValueError("malformed discourse post JSON, key 'raw' not found!")

    parsed_content = parse_raw_content(raw)

    topic_id = post_data.get("topic_id")
    if topic_id is None:
        raise ValueError("malformed discourse post JSON, key 'topic_id' not found!")

    topic_url = f"{base_url}/t/{topic_id}"
    res = requests.get(topic_url, headers=headers)
    topic_data = res.json()

    title = topic_data.get("title")
    if title is None:
        raise ValueError("malformed discourse topic JSON, key 'title' not found!")

    return {'title': title, 'external_discussion_url': topic_url, **parsed_content}


def import_discourse_topic_as_proposition(config: dict, import_info):
    base_url = config["base_url"]
    topic_id = int(import_info["topic_id"])

    topic_url = f"{base_url}/t/{topic_id}"

    headers = {'accept': 'application/json'}
    if  "api_key" in config:
        headers['api-key'] = config["api_key"]
        headers['api-username'] = config["api_username"]

    res = requests.get(topic_url, headers=headers)
    topic_data = res.json()

    title = topic_data.get("title")
    if title is None:
        raise ValueError("malformed discourse topic JSON, key 'title' not found!")

    post_id = topic_data.get("post_stream", {}).get("posts")[0]["id"]
    if post_id is None:
        raise ValueError("malformed discourse post JSON, id of first post not found!")

    post_url = f"{base_url}/posts/{post_id}"

    res = requests.get(post_url, headers=headers)
    post_data = res.json()

    raw = post_data.get("raw")
    if raw is None:
        raise ValueError("malformed discourse post JSON, key 'raw' not found!")

    parsed_content = parse_raw_content(raw)

    return {'title': title, 'external_discussion_url': topic_url, **parsed_content}

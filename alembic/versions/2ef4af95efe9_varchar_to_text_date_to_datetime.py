"""varchar->text everywhere, some date->datetime

Revision ID: 2ef4af95efe9
Revises: 9f82f82119dd
Create Date: 2020-08-15 15:28:18.853279

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ef4af95efe9'
down_revision = '9f82f82119dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('ballots', 'name',
               existing_type=sa.VARCHAR(length=64),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('changeset', 'section',
               existing_type=sa.VARCHAR(),
               type_=sa.Text(),
               existing_comment='Identifier for the section of the document that is changed.',
               existing_nullable=True)
    op.alter_column('customizable_text', 'lang',
               existing_type=sa.VARCHAR(length=16),
               type_=sa.Text())
    op.alter_column('customizable_text', 'name',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.Text())
    op.alter_column('departments', 'name',
               existing_type=sa.VARCHAR(length=64),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('document', 'lang',
               existing_type=sa.VARCHAR(length=16),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('document', 'name',
               existing_type=sa.VARCHAR(),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('groups', 'name',
               existing_type=sa.VARCHAR(length=64),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('page', 'lang',
               existing_type=sa.VARCHAR(length=16),
               type_=sa.Text())
    op.alter_column('page', 'name',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.Text())
    op.alter_column('page', 'title',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('policies', 'name',
               existing_type=sa.VARCHAR(length=64),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('propositions', 'voting_identifier',
               existing_type=sa.VARCHAR(length=10),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('propositiontypes', 'abbreviation',
               existing_type=sa.VARCHAR(length=10),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('propositiontypes', 'name',
               existing_type=sa.VARCHAR(length=64),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('secretvoters', 'last_change',
               existing_type=sa.DATE(),
               type_=sa.DateTime(),
               existing_nullable=False)
    op.alter_column('secretvoters', 'status',
               existing_type=sa.VARCHAR(length=10),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('subjectareas', 'name',
               existing_type=sa.VARCHAR(length=64),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('tags', 'name',
               existing_type=sa.VARCHAR(length=64),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('urnsupporters', 'type',
               existing_type=sa.VARCHAR(length=12),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('user_login_token', 'token',
               existing_type=sa.VARCHAR(length=36),
               type_=sa.Text())
    op.alter_column('userprofiles', 'sub',
               existing_type=sa.VARCHAR(length=64),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('users', 'auth_type',
               existing_type=sa.VARCHAR(length=8),
               type_=sa.Text(),
               existing_comment='deleted,system,token,virtual,oauth(has UserProfile)',
               existing_nullable=False,
               existing_server_default=sa.text("'system'::character varying"))
    op.alter_column('users', 'name',
               existing_type=sa.VARCHAR(length=64),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('voting_module', 'module_type',
               existing_type=sa.VARCHAR(length=16),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('voting_module', 'name',
               existing_type=sa.VARCHAR(length=16),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('votingphases', 'target',
               existing_type=sa.DATE(),
               type_=sa.DateTime(),
               existing_comment='constrained by §4.1',
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('votingphases', 'target',
               existing_type=sa.DateTime(),
               type_=sa.DATE(),
               existing_comment='constrained by §4.1',
               existing_nullable=True)
    op.alter_column('voting_module', 'name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=16),
               existing_nullable=False)
    op.alter_column('voting_module', 'module_type',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=16),
               existing_nullable=False)
    op.alter_column('users', 'name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=64),
               existing_nullable=False)
    op.alter_column('users', 'auth_type',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=8),
               existing_comment='deleted,system,token,virtual,oauth(has UserProfile)',
               existing_nullable=False,
               existing_server_default=sa.text("'system'::character varying"))
    op.alter_column('userprofiles', 'sub',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=64),
               existing_nullable=True)
    op.alter_column('user_login_token', 'token',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=36))
    op.alter_column('urnsupporters', 'type',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=12),
               existing_nullable=False)
    op.alter_column('tags', 'name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=64),
               existing_nullable=False)
    op.alter_column('subjectareas', 'name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=64),
               existing_nullable=False)
    op.alter_column('secretvoters', 'status',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=10),
               existing_nullable=False)
    op.alter_column('secretvoters', 'last_change',
               existing_type=sa.DateTime(),
               type_=sa.DATE(),
               existing_nullable=False)
    op.alter_column('propositiontypes', 'name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=64),
               existing_nullable=False)
    op.alter_column('propositiontypes', 'abbreviation',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=10),
               existing_nullable=False)
    op.alter_column('propositions', 'voting_identifier',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=10),
               existing_nullable=True)
    op.alter_column('policies', 'name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=64),
               existing_nullable=False)
    op.alter_column('page', 'title',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=255),
               existing_nullable=True)
    op.alter_column('page', 'name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=255))
    op.alter_column('page', 'lang',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=16))
    op.alter_column('groups', 'name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=64),
               existing_nullable=False)
    op.alter_column('document', 'name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(),
               existing_nullable=True)
    op.alter_column('document', 'lang',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=16),
               existing_nullable=True)
    op.alter_column('departments', 'name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=64),
               existing_nullable=False)
    op.alter_column('customizable_text', 'name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=255))
    op.alter_column('customizable_text', 'lang',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=16))
    op.alter_column('changeset', 'section',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(),
               existing_comment='Identifier for the section of the document that is changed.',
               existing_nullable=True)
    op.alter_column('ballots', 'name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=64),
               existing_nullable=True)

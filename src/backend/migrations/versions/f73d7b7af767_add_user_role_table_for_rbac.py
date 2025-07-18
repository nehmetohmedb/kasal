"""add_user_role_table_for_rbac

Revision ID: f73d7b7af767
Revises: 1f0183de606
Create Date: 2025-06-07 14:44:57.723909

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'f73d7b7af767'
down_revision: Union[str, None] = '1f0183de606'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('europa_park_hotels')
    op.drop_table('crew_id_mapping')
    op.drop_index('ix_data_processing_che_number', table_name='data_processing')
    op.drop_index('ix_data_processing_id', table_name='data_processing')
    op.drop_table('data_processing')
    op.drop_index('documentation_embeddings_embedding_idx', table_name='documentation_embeddings', postgresql_with={'lists': '100'}, postgresql_using='ivfflat')
    op.drop_index('ix_documentation_embeddings_id', table_name='documentation_embeddings')
    op.drop_index('ix_documentation_embeddings_source', table_name='documentation_embeddings')
    op.drop_index('ix_documentation_embeddings_title', table_name='documentation_embeddings')
    op.drop_table('documentation_embeddings')
    op.drop_index('ix_agents_created_by_email', table_name='agents')
    op.alter_column('crews', 'agent_ids',
               existing_type=postgresql.JSONB(astext_type=sa.Text()),
               type_=sa.JSON(),
               existing_nullable=True)
    op.alter_column('crews', 'task_ids',
               existing_type=postgresql.JSONB(astext_type=sa.Text()),
               type_=sa.JSON(),
               existing_nullable=True)
    op.alter_column('crews', 'nodes',
               existing_type=postgresql.JSONB(astext_type=sa.Text()),
               type_=sa.JSON(),
               existing_nullable=True)
    op.alter_column('crews', 'edges',
               existing_type=postgresql.JSONB(astext_type=sa.Text()),
               type_=sa.JSON(),
               existing_nullable=True)
    op.drop_index('ix_crews_created_by_email', table_name='crews')
    op.drop_index('ix_crews_temp_id', table_name='crews')
    op.drop_index('ix_crews_temp_name', table_name='crews')
    op.create_index(op.f('ix_crews_id'), 'crews', ['id'], unique=False)
    op.create_index(op.f('ix_crews_name'), 'crews', ['name'], unique=False)
    op.drop_constraint('engineconfig_engine_name_key', 'engineconfig', type_='unique')
    op.create_unique_constraint('_engine_config_uc', 'engineconfig', ['engine_name', 'config_key'])
    op.create_index('idx_execution_logs_tenant_exec_id', 'execution_logs', ['tenant_id', 'execution_id'], unique=False)
    op.create_index('idx_execution_logs_tenant_timestamp', 'execution_logs', ['tenant_id', 'timestamp'], unique=False)
    op.create_index(op.f('ix_execution_logs_tenant_email'), 'execution_logs', ['tenant_email'], unique=False)
    op.create_index(op.f('ix_execution_logs_tenant_id'), 'execution_logs', ['tenant_id'], unique=False)
    op.drop_index('ix_execution_trace_created_by_email', table_name='execution_trace')
    op.drop_column('execution_trace', 'created_by_email')
    op.drop_index('ix_executionhistory_created_by_email', table_name='executionhistory')
    op.create_index(op.f('ix_executionhistory_tenant_email'), 'executionhistory', ['tenant_email'], unique=False)
    op.create_index(op.f('ix_executionhistory_tenant_id'), 'executionhistory', ['tenant_id'], unique=False)
    op.drop_column('executionhistory', 'created_by_email')
    op.drop_index('ix_flow_executions_created_by_email', table_name='flow_executions')
    op.drop_index('ix_flow_executions_tenant_email', table_name='flow_executions')
    op.drop_index('ix_flow_executions_tenant_id', table_name='flow_executions')
    op.drop_column('flow_executions', 'tenant_id')
    op.drop_column('flow_executions', 'created_by_email')
    op.drop_column('flow_executions', 'tenant_email')
    op.drop_index('ix_flows_created_by_email', table_name='flows')
    op.drop_constraint('flows_crew_id_fkey', 'flows', type_='foreignkey')
    op.create_foreign_key(None, 'flows', 'crews', ['crew_id'], ['id'])
    op.drop_index('ix_prompttemplate_created_by_email', table_name='prompttemplate')
    op.alter_column('tasks', 'markdown',
               existing_type=sa.BOOLEAN(),
               nullable=True,
               existing_server_default=sa.text('false'))
    op.drop_index('ix_tasks_created_by_email', table_name='tasks')
    op.drop_index('ix_tools_created_by_email', table_name='tools')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_tools_created_by_email', 'tools', ['created_by_email'], unique=False)
    op.create_index('ix_tasks_created_by_email', 'tasks', ['created_by_email'], unique=False)
    op.alter_column('tasks', 'markdown',
               existing_type=sa.BOOLEAN(),
               nullable=False,
               existing_server_default=sa.text('false'))
    op.create_index('ix_prompttemplate_created_by_email', 'prompttemplate', ['created_by_email'], unique=False)
    op.drop_constraint(None, 'flows', type_='foreignkey')
    op.create_foreign_key('flows_crew_id_fkey', 'flows', 'crews', ['crew_id'], ['id'], ondelete='CASCADE')
    op.create_index('ix_flows_created_by_email', 'flows', ['created_by_email'], unique=False)
    op.add_column('flow_executions', sa.Column('tenant_email', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('flow_executions', sa.Column('created_by_email', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('flow_executions', sa.Column('tenant_id', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    op.create_index('ix_flow_executions_tenant_id', 'flow_executions', ['tenant_id'], unique=False)
    op.create_index('ix_flow_executions_tenant_email', 'flow_executions', ['tenant_email'], unique=False)
    op.create_index('ix_flow_executions_created_by_email', 'flow_executions', ['created_by_email'], unique=False)
    op.add_column('executionhistory', sa.Column('created_by_email', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_executionhistory_tenant_id'), table_name='executionhistory')
    op.drop_index(op.f('ix_executionhistory_tenant_email'), table_name='executionhistory')
    op.create_index('ix_executionhistory_created_by_email', 'executionhistory', ['created_by_email'], unique=False)
    op.add_column('execution_trace', sa.Column('created_by_email', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.create_index('ix_execution_trace_created_by_email', 'execution_trace', ['created_by_email'], unique=False)
    op.drop_index(op.f('ix_execution_logs_tenant_id'), table_name='execution_logs')
    op.drop_index(op.f('ix_execution_logs_tenant_email'), table_name='execution_logs')
    op.drop_index('idx_execution_logs_tenant_timestamp', table_name='execution_logs')
    op.drop_index('idx_execution_logs_tenant_exec_id', table_name='execution_logs')
    op.drop_constraint('_engine_config_uc', 'engineconfig', type_='unique')
    op.create_unique_constraint('engineconfig_engine_name_key', 'engineconfig', ['engine_name'], postgresql_nulls_not_distinct=False)
    op.drop_index(op.f('ix_crews_name'), table_name='crews')
    op.drop_index(op.f('ix_crews_id'), table_name='crews')
    op.create_index('ix_crews_temp_name', 'crews', ['name'], unique=False)
    op.create_index('ix_crews_temp_id', 'crews', ['id'], unique=False)
    op.create_index('ix_crews_created_by_email', 'crews', ['created_by_email'], unique=False)
    op.alter_column('crews', 'edges',
               existing_type=sa.JSON(),
               type_=postgresql.JSONB(astext_type=sa.Text()),
               existing_nullable=True)
    op.alter_column('crews', 'nodes',
               existing_type=sa.JSON(),
               type_=postgresql.JSONB(astext_type=sa.Text()),
               existing_nullable=True)
    op.alter_column('crews', 'task_ids',
               existing_type=sa.JSON(),
               type_=postgresql.JSONB(astext_type=sa.Text()),
               existing_nullable=True)
    op.alter_column('crews', 'agent_ids',
               existing_type=sa.JSON(),
               type_=postgresql.JSONB(astext_type=sa.Text()),
               existing_nullable=True)
    op.create_index('ix_agents_created_by_email', 'agents', ['created_by_email'], unique=False)
    op.create_table('documentation_embeddings',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('source', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('content', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('embedding', sa.NullType(), autoincrement=False, nullable=False),
    sa.Column('doc_metadata', postgresql.JSONB(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='documentation_embeddings_pkey')
    )
    op.create_index('ix_documentation_embeddings_title', 'documentation_embeddings', ['title'], unique=False)
    op.create_index('ix_documentation_embeddings_source', 'documentation_embeddings', ['source'], unique=False)
    op.create_index('ix_documentation_embeddings_id', 'documentation_embeddings', ['id'], unique=False)
    op.create_index('documentation_embeddings_embedding_idx', 'documentation_embeddings', ['embedding'], unique=False, postgresql_with={'lists': '100'}, postgresql_using='ivfflat')
    op.create_table('data_processing',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('che_number', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('processed', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('tax_validity', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('legal_name', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('address', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('activity_status', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('contact_name', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('phone', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('email', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('company_name', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='data_processing_pkey')
    )
    op.create_index('ix_data_processing_id', 'data_processing', ['id'], unique=False)
    op.create_index('ix_data_processing_che_number', 'data_processing', ['che_number'], unique=True)
    op.create_table('crew_id_mapping',
    sa.Column('old_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('new_id', sa.UUID(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('old_id', name='crew_id_mapping_pkey')
    )
    op.create_table('europa_park_hotels',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('hotel_name', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('website', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('availability', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('price_april_23', sa.REAL(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='europa_park_hotels_pkey')
    )
    # ### end Alembic commands ### 
"""1.0

Revision ID: 6a5653cfee9e
Revises: 
Create Date: 2024-02-23 19:28:44.185005

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6a5653cfee9e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('avatars',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('photo_path', sa.String(), nullable=False),
    sa.Column('photo_thumb', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('blood_components',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('icon', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_blood_components_title'), 'blood_components', ['title'], unique=True)
    op.create_table('blood_groups',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_blood_groups_title'), 'blood_groups', ['title'], unique=True)
    op.create_table('pet_types',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('icon', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pet_types_title'), 'pet_types', ['title'], unique=True)
    op.create_table('regions',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_regions_title'), 'regions', ['title'], unique=True)
    op.create_table('rhesus',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_rhesus_title'), 'rhesus', ['title'], unique=True)
    op.create_table('user_networks',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('telegram', sa.String(), nullable=False),
    sa.Column('vk', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_roles',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_roles_title'), 'user_roles', ['title'], unique=True)
    op.create_table('vaccinations',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_vaccinations_title'), 'vaccinations', ['title'], unique=True)
    op.create_table('breeds',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('pet_type_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['pet_type_id'], ['pet_types.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_breeds_title'), 'breeds', ['title'], unique=True)
    op.create_table('cities',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('region_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['region_id'], ['regions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_cities_title'), 'cities', ['title'], unique=True)
    op.create_table('pet_blood_groups',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('blood_group_id', sa.Integer(), nullable=False),
    sa.Column('pet_type_id', sa.Integer(), nullable=False),
    sa.Column('rhesus_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['blood_group_id'], ['blood_groups.id'], ),
    sa.ForeignKeyConstraint(['pet_type_id'], ['pet_types.id'], ),
    sa.ForeignKeyConstraint(['rhesus_id'], ['rhesus.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pet_blood_groups_blood_group_id'), 'pet_blood_groups', ['blood_group_id'], unique=False)
    op.create_table('clinics',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=False),
    sa.Column('city_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['city_id'], ['cities.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_clinics_address'), 'clinics', ['address'], unique=True)
    op.create_index(op.f('ix_clinics_email'), 'clinics', ['email'], unique=True)
    op.create_index(op.f('ix_clinics_phone'), 'clinics', ['phone'], unique=True)
    op.create_index(op.f('ix_clinics_title'), 'clinics', ['title'], unique=True)
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('surname', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('patronymic', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('user_role_id', sa.Integer(), nullable=False),
    sa.Column('city_id', sa.Integer(), nullable=False),
    sa.Column('avatar_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['avatar_id'], ['avatars.id'], ),
    sa.ForeignKeyConstraint(['city_id'], ['cities.id'], ),
    sa.ForeignKeyConstraint(['user_role_id'], ['user_roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('pets',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('blood_group_id', sa.Integer(), nullable=False),
    sa.Column('breed_id', sa.Integer(), nullable=False),
    sa.Column('breed', sa.String(), nullable=False),
    sa.Column('pet_type_id', sa.Integer(), nullable=False),
    sa.Column('avatar_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('weight', sa.Float(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['avatar_id'], ['avatars.id'], ),
    sa.ForeignKeyConstraint(['blood_group_id'], ['pet_blood_groups.id'], ),
    sa.ForeignKeyConstraint(['breed_id'], ['breeds.id'], ),
    sa.ForeignKeyConstraint(['pet_type_id'], ['pet_types.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users_configs',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('phone_number_status', sa.Integer(), nullable=False),
    sa.Column('social_networks_status', sa.Integer(), nullable=False),
    sa.Column('email_status', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_configs_email_status'), 'users_configs', ['email_status'], unique=False)
    op.create_index(op.f('ix_users_configs_phone_number_status'), 'users_configs', ['phone_number_status'], unique=False)
    op.create_index(op.f('ix_users_configs_social_networks_status'), 'users_configs', ['social_networks_status'], unique=False)
    op.create_table('demands',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('reason', sa.Text(), nullable=False),
    sa.Column('blood_component_id', sa.Integer(), nullable=False),
    sa.Column('blood_amount', sa.Integer(), nullable=False),
    sa.Column('donor_amount', sa.Integer(), nullable=False),
    sa.Column('pet_id', sa.Integer(), nullable=False),
    sa.Column('clinic_id', sa.Integer(), nullable=False),
    sa.Column('end_actual_date', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['blood_component_id'], ['blood_components.id'], ),
    sa.ForeignKeyConstraint(['clinic_id'], ['clinics.id'], ),
    sa.ForeignKeyConstraint(['pet_id'], ['pets.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pet__vaccinations',
    sa.Column('pet_id', sa.Integer(), nullable=False),
    sa.Column('vaccination_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['pet_id'], ['pets.id'], ),
    sa.ForeignKeyConstraint(['vaccination_id'], ['vaccinations.id'], ),
    sa.PrimaryKeyConstraint('pet_id', 'vaccination_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pet__vaccinations')
    op.drop_table('demands')
    op.drop_index(op.f('ix_users_configs_social_networks_status'), table_name='users_configs')
    op.drop_index(op.f('ix_users_configs_phone_number_status'), table_name='users_configs')
    op.drop_index(op.f('ix_users_configs_email_status'), table_name='users_configs')
    op.drop_table('users_configs')
    op.drop_table('pets')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_clinics_title'), table_name='clinics')
    op.drop_index(op.f('ix_clinics_phone'), table_name='clinics')
    op.drop_index(op.f('ix_clinics_email'), table_name='clinics')
    op.drop_index(op.f('ix_clinics_address'), table_name='clinics')
    op.drop_table('clinics')
    op.drop_index(op.f('ix_pet_blood_groups_blood_group_id'), table_name='pet_blood_groups')
    op.drop_table('pet_blood_groups')
    op.drop_index(op.f('ix_cities_title'), table_name='cities')
    op.drop_table('cities')
    op.drop_index(op.f('ix_breeds_title'), table_name='breeds')
    op.drop_table('breeds')
    op.drop_index(op.f('ix_vaccinations_title'), table_name='vaccinations')
    op.drop_table('vaccinations')
    op.drop_index(op.f('ix_user_roles_title'), table_name='user_roles')
    op.drop_table('user_roles')
    op.drop_table('user_networks')
    op.drop_index(op.f('ix_rhesus_title'), table_name='rhesus')
    op.drop_table('rhesus')
    op.drop_index(op.f('ix_regions_title'), table_name='regions')
    op.drop_table('regions')
    op.drop_index(op.f('ix_pet_types_title'), table_name='pet_types')
    op.drop_table('pet_types')
    op.drop_index(op.f('ix_blood_groups_title'), table_name='blood_groups')
    op.drop_table('blood_groups')
    op.drop_index(op.f('ix_blood_components_title'), table_name='blood_components')
    op.drop_table('blood_components')
    op.drop_table('avatars')
    # ### end Alembic commands ###

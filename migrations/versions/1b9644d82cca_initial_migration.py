"""Initial migration.

Revision ID: 1b9644d82cca
Revises: 
Create Date: 2024-07-29 20:14:23.086546

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '1b9644d82cca'
down_revision = None
branch_labels = None
depends_on = None

# Define the metadata object
metadata = sa.MetaData()

# Define the supplier table
supplier_table = sa.Table(
    'supplier',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('logo', sa.String(length=200), nullable=False),
    sa.Column('state', sa.String(length=50), nullable=False),
    sa.Column('cost_per_kwh', sa.Float(), nullable=False),
    sa.Column('min_kwh', sa.Integer(), nullable=False),
    sa.Column('total_clients', sa.Integer(), nullable=False),
    sa.Column('avg_rating', sa.Float(), nullable=False)
)


def upgrade():
    # Create the supplier table
    op.create_table(
        'supplier',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('logo', sa.String(length=200), nullable=False),
        sa.Column('state', sa.String(length=50), nullable=False),
        sa.Column('cost_per_kwh', sa.Float(), nullable=False),
        sa.Column('min_kwh', sa.Integer(), nullable=False),
        sa.Column('total_clients', sa.Integer(), nullable=False),
        sa.Column('avg_rating', sa.Float(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema=None
    )

    # Insert data into the supplier table
    op.bulk_insert(supplier_table, [
        {"id": 1, "name": "2W Energia",
         "logo": "https://media.glassdoor.com/sqll/4273031/2w-energia-squarelogo-1647420984815.png",
         "state": "São Paulo", "cost_per_kwh": 0.45, "min_kwh": 2000, "total_clients": 1500, "avg_rating": 4.4},
        {"id": 2, "name": "Abengoa", "logo": "https://uploads.jornalcana.com.br/2016/02/aben.jpeg",
         "state": "Rio de Janeiro", "cost_per_kwh": 0.48, "min_kwh": 2500, "total_clients": 1200, "avg_rating": 4.2},
        {"id": 3, "name": "AES Brasil", "logo": "https://s3-symbol-logo.tradingview.com/aes-brasil--600.png",
         "state": "São Paulo", "cost_per_kwh": 0.47, "min_kwh": 2200, "total_clients": 1300, "avg_rating": 4.3},
        {"id": 4, "name": "Casa dos Ventos",
         "logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTcV6RBZTTFo5R9etOhZ_OZrMudTkT4fII9Mw&s",
         "state": "Ceará", "cost_per_kwh": 0.44, "min_kwh": 2300, "total_clients": 1100, "avg_rating": 4.5},
        {"id": 5, "name": "Eneva",
         "logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTxQjzRs2LOkuT-c3kF6lp0Rvz-mkmnXNrZ-g&s",
         "state": "Maranhão", "cost_per_kwh": 0.46, "min_kwh": 2400, "total_clients": 1000, "avg_rating": 4.0},
        {"id": 6, "name": "Engie Brasil",
         "logo": "https://yt3.googleusercontent.com/2EgBZrfJVHlJdfK1p33eTc60j3j_0NJriJ0_NDnEvfNhCwajI69rXsJV2AwqTl3wIIEMtXbFpw=s900-c-k-c0x00ffffff-no-rj",
         "state": "Santa Catarina", "cost_per_kwh": 0.49, "min_kwh": 2100, "total_clients": 1600, "avg_rating": 4.6},
        {"id": 7, "name": "Enel Green Power",
         "logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSkVnvd4-3Oeu6TjPEISUKWB_dbRBh67wltfg&s",
         "state": "São Paulo", "cost_per_kwh": 0.47, "min_kwh": 2200, "total_clients": 1700, "avg_rating": 4.4},
        {"id": 8, "name": "Iberdrola Renováveis Brasil",
         "logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQHDM4jNO1tFsGecsvg",
         "state": "São Paulo", "cost_per_kwh": 0.50, "min_kwh": 2000, "total_clients": 1000, "avg_rating": 4.3},
        {"id": 9, "name": "Omega Energia",
         "logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT8dtfwgDsrE44Agv9VdJC_VcHWR_Artut4MQ&s",
         "state": "Minas Gerais", "cost_per_kwh": 0.42, "min_kwh": 2300, "total_clients": 1900, "avg_rating": 4.3},
        {"id": 10, "name": "EDP Renováveis Brasil",
         "logo": "https://logodownload.org/wp-content/uploads/2017/08/edp-logo-0.png", "state": "Espírito Santo",
         "cost_per_kwh": 0.45, "min_kwh": 2100, "total_clients": 1400, "avg_rating": 4.5},
        {"id": 11, "name": "CPFL Renováveis",
         "logo": "https://media.licdn.com/dms/image/C4E0BAQEuRURj_jSr2g/company-logo_200_200/0/1631328851340?e=2147483647&v=beta&t=8ZiVxySo1wIGliAOst_gaSsIpLztqSyEGRGX7VjHIZs",
         "state": "São Paulo", "cost_per_kwh": 0.5, "min_kwh": 2500, "total_clients": 1600, "avg_rating": 4.4},
        {"id": 12, "name": "Renova Energia",
         "logo": "https://www.abgd.com.br/portal/wp-content/uploads/jet-engine-forms/7/2022/10/280881424_4986427788059639_2079786146419613029_n.jpg",
         "state": "Minas Gerais", "cost_per_kwh": 0.48, "min_kwh": 2200, "total_clients": 1300, "avg_rating": 4.3},
        {"id": 13, "name": "Solatio Energia",
         "logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSyA5xImavZhk0_0bqeu3H2A_GQpTW34gbeJRoW3iPit2Kf1WZvczQVTMuelkqmQSfGp9E&usqp=CAU",
         "state": "Pernambuco", "cost_per_kwh": 0.43, "min_kwh": 2400, "total_clients": 1500, "avg_rating": 4.5},
        {"id": 14, "name": "Blue Sol Energia Solar",
         "logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRct6SwhBxl7_6Pthg8gWD9yhXLo6A-afVdQw&s",
         "state": "São Paulo", "cost_per_kwh": 0.45, "min_kwh": 2200, "total_clients": 1100, "avg_rating": 4.2},
        {"id": 15, "name": "Alsol Energias Renováveis",
         "logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTxQjzRs2LOkuT-c3kF6lp0Rvz-mkmnXNrZ-g&s",
         "state": "Minas Gerais", "cost_per_kwh": 0.46, "min_kwh": 2300, "total_clients": 1200, "avg_rating": 4.4},
        {"id": 16, "name": "Cemig",
         "logo": "https://assets.hgbrasil.com/finance/companies/big/cemig.png",
         "state": "Minas Gerais", "cost_per_kwh": 0.47, "min_kwh": 2300, "total_clients": 1700, "avg_rating": 4.3},
        {"id": 17, "name": "Alupar",
         "logo": "https://media.licdn.com/dms/image/C4E0BAQHOgCxiV073oA/company-logo_200_200/0/1631325214086?e=2147483647&v=beta&t=qF0bjNCVlkjMBUEfjOjzLp4PJjXlhk2I9aCXfapPMEA",
         "state": "São Paulo", "cost_per_kwh": 0.44, "min_kwh": 2000, "total_clients": 1800, "avg_rating": 4.5},
        {"id": 18, "name": "Neonergia",
         "logo": "https://play-lh.googleusercontent.com/dLS3GhNV8r2rDzUK-nL1Yg0SWjO0smadHnPe8UU54u5Tejvcrd0poKYIhPQqIT7uGLU",
         "state": "Bahia", "cost_per_kwh": 0.42, "min_kwh": 2400, "total_clients": 1500, "avg_rating": 4.4},
        {"id": 19, "name": "Volta Energia",
         "logo": "https://media.licdn.com/dms/image/C4E0BAQEpXldE5hcHrw/company-logo_200_200/0/1630655206710?e=2147483647&v=beta&t=iErSJV-6f_oxsbGgjG009wG_mix4pnrtfnGWMy6FJHE",
         "state": "Rio de Janeiro", "cost_per_kwh": 0.41, "min_kwh": 2500, "total_clients": 1600, "avg_rating": 4.2},
        {"id": 20, "name": "Canadian Solar",
         "logo": "https://asset.brandfetch.io/id3fpve49Z/idFiIYtAOm.jpeg",
         "state": "São Paulo", "cost_per_kwh": 0.48, "min_kwh": 2100, "total_clients": 1400, "avg_rating": 4.3}
    ])


def downgrade():
    op.drop_table('supplier')

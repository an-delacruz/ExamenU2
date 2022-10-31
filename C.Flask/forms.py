from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField,DecimalField
from wtforms.validators import DataRequired

class LaptopForm(FlaskForm):
    marca = StringField('Marca',validators=[DataRequired()],render_kw={"placeholder": "Marca"})
    modelo = StringField('Modelo',render_kw={"placeholder": "Placas"})
    color = StringField('Color',render_kw={"placeholder": "Color"})
    precio = DecimalField('Precio',validators=[DataRequired()],render_kw={"placeholder": "Precio"})
    unidades = IntegerField('Unidades',render_kw={"placeholder": "Unidades"})
    enviar = SubmitField('Enviar')

class TecladoForm(FlaskForm):
    marca = StringField('Marca',validators=[DataRequired()],render_kw={"placeholder": "Marca"})
    modelo = StringField('Modelo',render_kw={"placeholder": "Placas"})
    precio = DecimalField('Precio',validators=[DataRequired()],render_kw={"placeholder": "Precio"})
    unidades = IntegerField('Unidades',render_kw={"placeholder": "Unidades"})
    enviar = SubmitField('Enviar')

class MouseForm(FlaskForm):
    marca = StringField('Marca',validators=[DataRequired()],render_kw={"placeholder": "Marca"})
    modelo = StringField('Modelo',render_kw={"placeholder": "Placas"})
    precio = DecimalField('Precio',validators=[DataRequired()],render_kw={"placeholder": "Precio"})
    unidades = IntegerField('Unidades',render_kw={"placeholder": "Unidades"})
    enviar = SubmitField('Enviar')
# -*- coding: utf-8 -*-
from django.db import models
from Campeonatos.models import Campeonato
from Jugadores.models import Jugador


# Create your models here.
class Inscripcion(models.Model):
	campeonato	= models.ForeignKey(Campeonato)
	jugador		= models.ForeignKey(Jugador)
	pago 		= models.Field(max_length=50)
	
	
	class Meta:
		verbose_name = 'Incripcione'
		verbose_name_plural = 'Incripciones'

	def __unicode__(self):
		return 'Campeonato:'+self.campeonato.nombre+',Jugador:'+self.jugador.nombre

	def __str__(self):
		return '%s %s %s %s' % ('Campeonato',self.campeonato.nombre,'Jugador:',self.jugador.nombre) 

		

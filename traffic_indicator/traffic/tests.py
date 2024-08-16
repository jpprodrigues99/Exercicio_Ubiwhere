from django.test import TestCase
from .models import RoadSegment

class RoadSegmentTestCase(TestCase):
    
    def setUp(self):
        
        self.segment1 = RoadSegment.objects.create(
            long_start=10.0, lat_start=10.0, long_end=20.0, lat_end=20.0,
            length=10.0, speed=15.0
        )
        self.segment2 = RoadSegment.objects.create(
            long_start=30.0, lat_start=30.0, long_end=40.0, lat_end=40.0,
            length=10.0, speed=30.0
        )
        self.segment3 = RoadSegment.objects.create(
            long_start=50.0, lat_start=50.0, long_end=60.0, lat_end=60.0,
            length=10.0, speed=60.0
        )
    
    def test_intensity_low(self):
        """ Testa se a intensidade é 'elevada' quando a velocidade é <= 20 """
        self.assertEqual(self.segment1.intensity, 'elevada')

    def test_intensity_medium(self):
        """ Testa se a intensidade é 'média' quando a velocidade é > 20 e <= 50 """
        self.assertEqual(self.segment2.intensity, 'média')

    def test_intensity_high(self):
        """ Testa se a intensidade é 'baixa' quando a velocidade é > 50 """
        self.assertEqual(self.segment3.intensity, 'baixa')

    def test_default_values(self):
        """ Testa se os valores padrão são definidos corretamente """
        segment = RoadSegment.objects.create(
            long_start=0.0, lat_start=0.0, long_end=0.0, lat_end=0.0
        )
        self.assertEqual(segment.length, 0.0)
        self.assertEqual(segment.speed, 0.0)

from django.db import models

class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_migrations'

class TPenerbit(models.Model):
	id_penerbit = models.IntegerField(primary_key=True)  # This field type is a guess.
	nama_penerbit = models.CharField(max_length=50, blank=True, null=True)
	kota_penerbit = models.CharField(max_length=50, blank=True, null=True)

	class Meta:
		managed = True #true, berarti dapat melakukan editing data di basis data
		db_table = 't_penerbit' #nama tabel di basis data

class TPengarang(models.Model):
	id_pengarang = models.IntegerField(primary_key=True)
	nama_pengarang = models.CharField(max_length=100, blank=True, null=True)

	class Meta:
		managed = True #true, berarti dapat melakukan editing data di basis data
		db_table = 't_pengarang' #nama tabel di basis data		

class TKategori(models.Model):
    id_kategori = models.IntegerField(primary_key=True)
    kategori = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True #true, berarti dapat melakukan editing data di basis data
        db_table = 't_kategori'	 #nama tabel di basis data	
		
class TBuku(models.Model):
	id_buku = models.TextField(primary_key=True)
	judul_buku = models.CharField(max_length=256, blank=True, null=True)
	id_penerbit = models.ForeignKey('TPenerbit', models.DO_NOTHING, db_column='id_penerbit', blank=True,null=True)
	id_kategori = models.ForeignKey('TKategori', models.DO_NOTHING, db_column='id_kategori', blank=True,null=True)
	id_pengarang = models.ForeignKey('TPengarang', models.DO_NOTHING, db_column='id_pengarang', blank=True,null=True)
	tahun_terbit = models.CharField(max_length=4, blank=True, null=True)

	class Meta:
		managed = True #true, berarti dapat melakukan editing data di basis data
		db_table = 't_buku' #nama tabel di basis data





		
class TKota(models.Model):
	id = models.CharField(primary_key=True, max_length=50)
	lat = models.FloatField(blank=True, null=True)
	long = models.FloatField(blank=True, null=True)
	jum = models.IntegerField(blank=True, null=True)
	
	class Meta:
		managed = True
		db_table = 't_kota'
		

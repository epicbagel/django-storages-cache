from django.conf import settings
from storages.backends.mosso import CloudFilesStorage
from cumulus.storage import CloudFilesStaticStorage
from django.contrib.staticfiles.storage import CachedFilesMixin

class MyCachedFilesMixin(CachedFilesMixin):
	def url(self, *a, **kw):
		import urlparse, urllib
		s = super(MyCachedFilesMixin, self).url(*a, **kw)
		if isinstance(s, unicode):
			s = s.encode('utf-8', 'ignore')
		scheme, netloc, path, qs, anchor = urlparse.urlsplit(s)
		path = urllib.quote(path, '/%')
		qs = urllib.quote_plus(qs, ':&=')
		return urlparse.urlunsplit((scheme, netloc, path, qs, anchor))

class CachedStaticCloudFilesStorage(MyCachedFilesMixin, CloudFilesStaticStorage):
	def __init__(self, *args, **kwargs):
		super(CachedStaticCloudFilesStorage, self).__init__(*args, **kwargs)

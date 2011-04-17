from django.db import models
from django.utils.translation import ugettext as _

class Room(models.Model):
    "The room or place where the session is set."
    name = models.CharField(_('room'), max_length=50)

    class Meta:
        verbose_name = _('room')
        verbose_name_plural = _('rooms')

    def __unicode__(self):
        return u'%s' % self.name


class Session(models.Model):
    "The session description."
    topic_title = models.CharField(_('topic title'), max_length=255, default=_('unknown'))
    room = models.ForeignKey(Room)
    start_time = models.DateTimeField(_('start time'))
    end_time = models.DateTimeField(_('end time'))
    description = models.TextField(_('description'), blank=True)
    speaker = models.CharField(_('speaker'), blank=True, max_length=100,
        help_text=_('you may indicate here the speaker / leader of this session'))

    class Meta:
        verbose_name = _('session')
        verbose_name_plural = _('sessions')

    def __unicode__(self):
        return u'%s' % self.topic_title

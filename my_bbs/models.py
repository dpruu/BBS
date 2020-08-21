from django.db import models


class Board(models.Model):
    author = models.CharField('작성자', max_length=20)
    title = models.CharField('제목', max_length=20)
    contents = models.TextField('글내용', max_length=1000)
    Good = models.IntegerField(default=0)
    Bad = models.IntegerField(default=0)

    def __str__(self):
        return self.contents


class Comment(models.Model):
    board_id = models.ForeignKey(Board, on_delete=models.CASCADE, blank=True, default=0)
    author = models.CharField('작성자', max_length=20)
    contents = models.TextField('글내용', max_length=1000)

    def __str__(self):
        return self.contents

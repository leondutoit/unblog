
import pytumblr
import bs4

class TumblrBlogPost(object):

    """Stores tumblr blog post information"""

    def __init__(self, raw_content):
        self.title = self._title_from_raw(raw_content)
        self.text = self._text_from_raw(raw_content)
        self.tags = self._tags_from_raw(raw_content)
        self.media_urls = self._media_urls_from_raw(raw_content)

    def _title_from_raw(self, raw_content):
        return raw_content['title']

    def _text_from_raw(self, raw_content):
        """Note links are put into _text_from_raw"""
        text = raw_content['trail'][0]['content_raw']
        soup = bs4.BeautifulSoup(text)
        for link in soup.findAll('a'):
            link.replace_with(link.get('href'))
        return soup.text

    def _tags_from_raw(self, raw_content):
        return raw_content['tags']

    def _media_urls_from_raw(self, raw_content):
        text = raw_content['trail'][0]['content_raw']
        soup = bs4.BeautifulSoup(text)
        urls = map(lambda x: x.get('src'), soup.findAll('img'))
        if urls is None:
            return []
        else:
            return urls

    def to_dict(self):
        return {
            "title": self.title,
            "text": self.text,
            "tags": self.tags,
            "media_urls": self.media_urls
        }

    def to_dir(self, path):
        pass


class Blog(object):

    def __init__(self, client, blog_name):
        self.name = blog_name
        self.posts = self._objectify(self._get_all_posts(client, blog_name))

    def _create_post(self, raw_content):
        return TumblrBlogPost(raw_content)

    def _get_posts(self, client, blog_name, offset):
        return client.posts(blog_name, offset = offset)

    def _objectify(self, posts):
        blog_objects = []
        for post in posts:
            blog_objects.append(TumblrBlogPost(post))
        return blog_objects

    def _get_all_posts(self, client, blog_name):
        all_posts = []
        offset = 0
        while True:
            print "getting posts for %s" % blog_name
            resp = self._get_posts(client, blog_name, offset)
            all_posts.extend(resp['posts'])
            offset += len(resp['posts'])
            if offset >= resp['total_posts']:
                break
        return all_posts

    def to_dicts(self):
        return map(lambda x: x.to_dict(), self.posts)

    def to_dir(self, path):
        pass


class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = []
        for i in range(self.pages):
            self.photos.append([])

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = int(photos_count / 4)
        return cls(pages)

    def add_photo(self, label):
        for r in range(self.pages):
            while len(self.photos[r]) < 4:
                self.photos[r].append(label)
                return f"{label} photo added successfully on page {r + 1} slot {len(self.photos[r])}"
        return "No more free spots"

    def display(self):
        result = ''
        for r in range(self.pages):
            result += '-----------\n'
            result_photo = ''
            while self.photos[r]:
                result_photo += "[] "
                self.photos[r].pop()
            result_photo = result_photo[:-1]
            result += (result_photo + '\n')
        result += '-----------\n'
        return result


album = PhotoAlbum(3)
for _ in range(8):
    album.add_photo("asdf")

print(album.display())

album_1 = PhotoAlbum(1)
album_1.add_photo("baby")
album_1.add_photo("first grade")
album_1.add_photo("eight grade")
album_1.add_photo("party with friends")
print(album_1.display())

import unittest


class TestsPhotoAlbum(unittest.TestCase):
    def test_init_creates_all_attributes(self):
        album = PhotoAlbum(2)
        self.assertEqual(album.pages, 2)
        self.assertEqual(album.photos, [[], []])

    def test_from_photos_should_create_instace(self):
        album = PhotoAlbum.from_photos_count(12)
        self.assertEqual(album.pages, 3)
        self.assertEqual(album.photos, [[], [], []])

    def test_add_photo_with_no_free_spots(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        result = album.add_photo("prom")
        self.assertEqual(result, "No more free spots")

    def test_add_photo_with_free_spots(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        self.assertEqual(album.photos, [['baby', 'first grade', 'eight grade', 'party with friends']])

    def test_display_with_one_page(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        result = album.display()
        self.assertEqual(result, "-----------\n[] [] [] []\n-----------\n")

    def test_display_with_three_pages(self):
        album = PhotoAlbum(3)
        for _ in range(8):
            album.add_photo("asdf")
        result = album.display()
        self.assertEqual(result, "-----------\n[] [] [] []\n-----------\n[] [] [] []\n-----------\n\n-----------\n")


if __name__ == "__main__":
    unittest.main()











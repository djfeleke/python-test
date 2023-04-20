"""Testsq for Balloonicorn's Flask app."""
from flask import Flask, request, session


import unittest
import party

class PartyTests(unittest.TestCase):
    """Tests for my party site."""

    def setUp(self):
        """Code to run before every test."""

        self.client = party.app.test_client()
        party.app.config['TESTING'] = True

    def test_homepage(self):
        """Can we reach the homepage?"""

        result = self.client.get("/")
        self.assertIn(b"having a party", result.data)

    def test_no_rsvp_yet(self):
        """Do users who haven't RSVPed see the correct view?"""
       
        result = self.client.get("/")
        self.assertIn(b"RSVP", result.data)

        
        # FIXME: Add a test to show we haven't RSVP'd yet
        

    def test_rsvp(self):
        """Do RSVPed users see the correct view?"""

        rsvp_info = {'name': "Jane", 'email': "jane@jane.com"}

        result = self.client.post("/rsvp", data=rsvp_info,
                                  follow_redirects=True)

        # FIXME: check that once we log in we see party details--but not the form!
        result = self.client.get("/")
        self.assertIn(b"Party Details", result.data)

        # print("FIXME")

    def test_rsvp_mel(self):
        """Can we keep Mel out?"""

        # FIXME: write a test that mel can't invite himself
        # result = self.client.get("/treats")
        # self.assertIn(b"Mel", result.data)
        assert request.args.get['name'] == 'mel'

if __name__ == "__main__":
    unittest.main()

import unittest
from athera.sync.client import Client
import os
import logging
import sys
import uuid
import datetime
import time

from settings import environment, compute_arguments


class SyncTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.token = os.getenv("ATHERA_API_TEST_TOKEN")
        if not cls.token:
            raise ValueError("ATHERA_API_TEST_TOKEN environment variable must be set")
        cls.client = Client(environment.ATHERA_API_TEST_REGION, cls.token)

    def test_get_mounts(self):
        """ Test we can get groups for the authenticated user.
        Will only work with Python 2. Python 3 will segfault - TODO check this still applies
        """
        mounts, err = self.client.get_mounts(
            environment.ATHERA_API_TEST_GROUP_ID,
        )
        self.assertIsNone(err, "Got unexpected error: {}".format(err))
        self.assertIsNotNone(mounts, "Expected response not to be None")
        self.assertGreaterEqual(len(mounts), 2, "Expected to get at least 2 mounts")


    def test_get_files(self):
        """ Test we can get files for the authenticated user.
        Will only work with Python 2. Python 3 will segfault - TODO check this still applies
        """
        filesGenerator = self.client.get_files(
            environment.ATHERA_API_TEST_GROUP_ID,
            environment.ATHERA_API_TEST_SYNC_API_MOUNT_ID,
            path=""
            )

        for _, err in filesGenerator:
            self.assertIsNone(err, "Got unexpected error: {}".format(err))

           

    def test_download(self):
        """ Test we can get files for the authenticated user.
        Will only work with Python 2. Python 3 will segfault - TODO check this still applies
        """

        files_to_download = []

        # List files in remote assets
        filesGenerator = self.client.get_files(
            environment.ATHERA_API_TEST_GROUP_ID,
            environment.ATHERA_API_TEST_SYNC_API_MOUNT_ID,
            path=environment.ATHERA_API_TEST_REMOTE_ASSETS_FOLDER
            )

        for sirius_file, err in filesGenerator:
            self.assertIsNone(err, "Got unexpected error: {}".format(err))
            files_to_download.append(sirius_file)


        for sirius_file in files_to_download:
            download_path = os.path.join(environment.ATHERA_API_TEST_LOCAL_ASSETS_FOLDER, sirius_file.file.name)
            with open(download_path, "wb+") as f:
                startTime = datetime.datetime.now()
                err = self.client.download_to_file(
                    environment.ATHERA_API_TEST_GROUP_ID,
                    environment.ATHERA_API_TEST_SYNC_API_MOUNT_ID,
                    f,
                    path=sirius_file.file.path, 
                )
                duration = datetime.datetime.now() - startTime
                print("Download file {}, Elapsed time: {}". format(sirius_file.file.name, duration))
                self.assertIsNone(err, "Got unexpected error: {}".format(err))
            stats = os.stat(download_path) 
            self.assertEqual(
                stats.st_size, 
                sirius_file.file.size, 
                "Expected downloaded file ({}) to contains 30 bytes; It contains instead {} bytes".format(environment.ATHERA_API_TEST_DONWLOAD_FILE_PATH, stats.st_size)
            )

    def test_download_file_with_folder_path(self):
        """ Negative Testing - Download a folder.
        The api call should return an error as the provided path is the one of a directory.
        """
        download_path = "downloaded_file.txt"
        with open(download_path, "wb+") as f:
            print(date.now())
            err = self.client.download_to_file(
                environment.ATHERA_API_TEST_GROUP_ID,
                environment.ATHERA_API_TEST_SYNC_API_MOUNT_ID,
                f,
                path=environment.ATHERA_API_TEST_REMOTE_ASSETS_FOLDER,
                chunk_size=5
            )
            self.assertIsNotNone(err, "Expected an error but got None")
       
    def test_download_wrong_chunk_size(self):
        """ Test we can get files for the authenticated user.
        Will only work with Python 2. Python 3 will segfault - TODO check this still applies
        """
        value_error_raised = False
        download_path = os.path.join(environment.ATHERA_API_TEST_LOCAL_ASSETS_FOLDER, "dummy_name.txt")
        with open(download_path, "wb+") as f:
            try:
                err = self.client.download_to_file(
                    environment.ATHERA_API_TEST_GROUP_ID,
                    environment.ATHERA_API_TEST_SYNC_API_MOUNT_ID,
                    f,
                    path="/", 
                    chunk_size=1024*1024*1024
                )
            except ValueError as e:
                value_error_raised = True
        self.assertTrue(value_error_raised, "Expected ValueError to be raised")            

    def test_upload(self):
        """ Test Upload files in assets folder: Need test_download to be successful        
        """
        for filename in os.listdir(environment.ATHERA_API_TEST_LOCAL_ASSETS_FOLDER):
            destination_path = "uploads/" + filename
            filepath = os.path.join(environment.ATHERA_API_TEST_LOCAL_ASSETS_FOLDER, filename)
            with open(filepath, "rb") as f:
                startTime = datetime.datetime.now()
                _, err = self.client.upload_file(
                    environment.ATHERA_API_TEST_GROUP_ID,
                    environment.ATHERA_API_TEST_SYNC_API_MOUNT_ID,
                    f,
                    destination_path=destination_path,
                )
                duration = datetime.datetime.now() - startTime
                print("Uploaded file {}, Elapsed time: {}". format(filename, duration))
                self.assertIsNone(err, "Got unexpected error: {}".format(err))
                
    def test_upload_wrong_chunk_size(self):
        """ Test Upload files in assets folder: Need test_download to be successful        
        """
        value_error_raised = False
        filepath = "nose.cfg"
        with open(filepath, "rb") as f:
            try:
                _, err = self.client.upload_file(
                    environment.ATHERA_API_TEST_GROUP_ID,
                    environment.ATHERA_API_TEST_GROUP_MOUNT_ID,
                    f,
                    destination_path="/",
                    chunk_size=1024*1024*1024
                )
            except ValueError:
                value_error_raised = True
        self.assertTrue(value_error_raised, "Expected ValueError to be raised")  

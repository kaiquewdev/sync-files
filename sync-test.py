import unittest, sync

class SyncTest( unittest.TestCase ):
    def default_path( self ):
        return '/Users/kaiquesilva/Dropbox/PhoenixProjects/PDFs/gordo'

    def test_open_file_format_json( self ):
        file_path = '%s/update.json' % ( self.default_path() )
        file_test = sync.get_json( file_path ) 

        self.assertEquals( True, len( file_test ) > 0 )

    def test_sync_files( self ):
        file_path = '%s/update.json' % ( self.default_path() )
        update_format = sync.get_json( file_path )

        self.assertEquals( True, sync.files( update_format, self.default_path() ) )
        
if __name__ == '__main__':
    unittest.main()

import unittest, sync

class SyncTest( unittest.TestCase ):
    def default_path( self ):
        return '/Users/kaiquesilva/Dropbox/PhoenixProjects/PDFs'

    def test_open_file_format_json( self ):
        file_path = '%s/gordo/update.json' % ( self.default_path() )
        file_test = sync.get_json( file_path ) 

        self.assertEquals( True, len( file_test ) > 0 )

    def test_copy_of_a_file( self ):
        import os
        origin_path = './test_files/go-board.txt'
        destiny_path = './test_files/go-board-rules.txt'

        self.assertEquals( True, sync.copy( origin_path, destiny_path ) )

        os.remove( destiny_path )

    def sync_files( self ):
        file_path = '%s/gordo/update.json' % ( self.default_path() )
        update_format = sync.get_json( file_path )

        self.assertEquals( True, sync.files( update_format, self.default_path, 'gordo' ) )
        
if __name__ == '__main__':
    unittest.main()

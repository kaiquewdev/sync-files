#!/usr/bin/env python

def get_json( filename='' ):
    output = ''

    try:
        import json, os
        
        if filename and os.path.exists( filename ) :
            format_file = open( filename ).read()
            # Get file and translate to json
            format_file = json.loads( 
                format_file
                # Remove white spaces
                .replace( ' ', '' )
                # Remove line-breakers
                .replace( '\n', '' )
                # Change ' to "
                .replace( '\'', '\"' )
            )

            output = format_file

        return output
    except Exception:
        return output

def files( sync_format='', action_directory='' ):
    output = False

    try:
        import os

        if sync_format and os.path.exists( action_directory ):
            

    except Exception:
        return output

if __name__ == '__main__':
    pass
    # print get_json('/Users/kaiquesilva/Dropbox/PhoenixProjects/PDFs/gordo/update.json')

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

def copy( origin='', destiny='' ):
    output = False

    try:
        import os, shutil

        if os.path.exists( origin ) and not os.path.exists( destiny ):
            shutil.copy( origin, destiny )

            if os.path.exists( destiny ):
                output = True

        return output
    except Exception:
        return output

def files( sync_format='', main_directory='', action_directory='' ):
    import pdb; pdb.set_trace()
    output = False

    try:
        import os
        
        if sync_format and os.path.exists( main_directory ) and os.path.exists( '%s/%s' % ( main_directory, action_directory ) ):
            # Go to directory working directory
            os.chdir( main_directory ) 
            
            if action_directory in os.listdir('./'):
                for reference in sync_format:
                    paths = reference['link'].split('/')[3:]
                    destiny_path = ''
    
                    for path in paths:
                        destiny_path += path

                        if path in os.listdir('./'):
                            os.chdir( path )
                        if not path in os.listdir('./') and not paths[-1:] == path:
                            os.mkdir( './%s' % ( path ) )
                        if paths[-1:] == path and not os.exists( './%s' % ( path ) ):
                            output = copy( 
                                ( '%s/%s/%s' % ( main_directory, action_directory, path ) ),
                                ( destiny_path )
                            )

                            
                output = sync_format
        return output
    except Exception:
        return output

if __name__ == '__main__':
    default_path = '/Users/kaiquesilva/Dropbox/PhoenixProjects/PDFs'
    print files( get_json( '%s/gordo/update.json' % ( default_path ) ), default_path, 'gordo')
    # print get_json('/Users/kaiquesilva/Dropbox/PhoenixProjects/PDFs/gordo/update.json')

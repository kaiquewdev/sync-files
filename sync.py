#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
    output = False

    try:
        import os, json
        
        if os.path.exists( main_directory ) and os.path.exists( '%s/%s' % ( main_directory, action_directory ) ) and sync_format:
            # Go to directory working directory
            os.chdir( main_directory ) 
            
            if action_directory in os.listdir('./'):
                log_file = open( '{0}/logs.json'.format( main_directory ), 'w' )
                logs = []
                files_success = 0
                
                for reference in sync_format:
                    paths = reference['link'].split('/')[3:]
                    origin_path = ''
                    destiny_path = ''

    
                    for path in paths:
                        destiny_path += '/{0}'.format( path )
                        current_directory = os.listdir('./')
                        the_file = paths[-1:][0] == path
                        file_copy_success = False

                        if the_file:
                            origin_path = '{0}/{1}/{2}'.format( main_directory, action_directory, path )
                            destiny_path = '{0}{1}'.format( main_directory, destiny_path )

                            # Copy file to respectivity path
                            file_copy_success = copy(
                                origin_path,
                                destiny_path
                            )
                            
                            if file_copy_success and os.path.exists( destiny_path ):
                                files_success += 1
                                os.chdir( main_directory )
                                # Add to logs list the status of the file
                                logs.append( { 'link': reference['link'], 'status': 'copied', 'exists': os.path.exists( destiny_path ) } )
                            else:
                                os.chdir( main_directory )
                                logs.append( { 'link': reference['link'], 'status': 'not copied', 'exists': os.path.exists( destiny_path ) } )
                        if path in current_directory and not the_file:
                            os.chdir( path )
                        if not path in current_directory and not os.path.exists( './{0}'.format( path ) ) and not the_file:
                            os.mkdir( path )
                            os.chdir( path )
                if files_success == len( sync_format ):
                    output = True
                
                # Log the behavior
                log_file.write( json.dumps( logs ) )
                log_file.close()
        return output
    except Exception:
        return output

# default_path = '/Users/kaiquesilva/Dropbox/PhoenixProjects/PDFs'
# print files( get_json( '%s/gordo/update.json' % ( default_path ) ), default_path, 'gordo')
# print get_json('/Users/kaiquesilva/Dropbox/PhoenixProjects/PDFs/gordo/update.json')

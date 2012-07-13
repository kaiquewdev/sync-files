#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    '''
    Sync files, a CLI tools to copy files using a json file in the focused directory.
    '''
    import sys, sync
    import pdb; pdb.set_trace()
    
    # Arguments
    args = sys.argv
    # Parametized parameters
    parameters_name = [
        'sync-file',
        'working-directory',
        'focus-directory'
    ]

    # Find parameters in the sys argv
    parameters = {}

    if len( args ) > len( parameters_name ):
        for name in parameters_name:
            for arg in args:
                parameter = '--%s' % ( name )
                
                if parameter in args:
                    argid = args.index( parameter )

                    if arg == parameter and not args[ argid + 1 ].startswith('--'):
                        parameters[ name ] = args[ argid + 1 ]

        if ( 
            parameters.has_key( parameters_name[0] ) and \
            parameters.has_key( parameters_name[1] ) and \
            parameters.has_key( parameters_name[2] ) 
        ):
            # Sync files 
            sync.files( parameters[ parameters_name[0] ], parameters[ parameters_name[1] ], parameters[ parameters_name[2] ] )
            print 'Sync complete look at the log file!'
        else:
            print 'Parameters incorrect!'
    else:
        print 'Accepted parameters:'

        for name in parameters_name:
            print ' --%s' % ( name )

if __name__ == '__main__':
    main()

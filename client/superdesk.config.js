/**
 * This is the default configuration file for the Superdesk application. By default,
 * the app will use the file with the name "superdesk.config.js" found in the current
 * working directory, but other files may also be specified using relative paths with
 * the SUPERDESK_CONFIG environment variable or the grunt --config flag.
 */
module.exports = function(grunt) {
    return {
        apps: ['triangle.apps', 'superdesk-publisher'],
        importApps: ['../triangle', 'superdesk-publisher'],
        defaultRoute: '/workspace/personal',

        server: {
            url: 'http://localhost/api',
            ws: 'ws://localhost/ws'
        },

        view: {
            timeformat: 'HH:mm',
            dateformat: 'MM.DD.YYYY'
        },

        features: {
            preview: 1,
            swimlane: {columnsLimit: 4},
            noTakes: true,
            editor3: true,
            validatePointOfInterestForImages: false,
            editorHighlights: true,
            noPublishOnAuthoringDesk: true,
            noMissingLink: true
        },

        list: {
            'priority': [],
            'firstLine': [
                'headline'
            ],
            'secondLine': [
                'state',
                'embargo',
                'update',
                'expiry'
            ]
        },

	publisher: {
	    protocol: "http",
            tenant: '', // subdomain
            domain: '45.33.72.36', // IP address or domain name of your server where Superdesk Publisher is installed
            base: 'api/v2',

	    wsProtocol: 'ws',                /* ws or wss (websocket); if unspecified or '' defaults to 'wss' */
	    wsDomain: '45.33.72.36',  /* domain name (usually domain as above) */
                                      /* e.g.: example.com, abc.example.com */
                                      /* tenant, as above, is NOT used for websocket */
	    wsPath: '/ws',                    /* path to websocket root dir */
	    wsPort: '8080'
	}
    };
};

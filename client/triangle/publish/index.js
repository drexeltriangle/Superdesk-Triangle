// This file was modified from https://github.com/superdesk/superdesk-aap/blob/master/client/aap/publish/index.js

runConfig.$inject = ['adminPublishSettingsService', '$templateCache'];
function runConfig(adminPublishSettingsService, $templateCache) {
    // register new apple news publish service (Apple News)
    $templateCache.put(
        'triangle/publish/views/http-push-apple-news-config.html',
        require('./views/http-push-apple-news-config.html')
    );
    adminPublishSettingsService.registerTransmissionService('http_push_apple_news', {
        label: 'HTTP Push to Apple News',
        templateUrl: 'triangle/publish/views/http-push-apple-news-config.html',
    });
}

export default angular.module('triangle.apps.publish', [])
.run(runConfig);
"use strict";
var Project = (function () {
    function Project(id, name, gitUrl, topic, userid) {
        this.id = id;
        this.name = name;
        this.gitUrl = gitUrl;
        this.topic = topic;
        this.userid = userid;
    }
    return Project;
}());
exports.Project = Project;
//# sourceMappingURL=Project.js.map
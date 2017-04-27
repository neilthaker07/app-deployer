"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var core_1 = require("@angular/core");
var mock_projects_1 = require("./mock-projects");
var ProjectService = (function () {
    function ProjectService() {
        this.headers = new Headers({ 'Content-Type': 'application/json' });
    }
    ProjectService.prototype.getProjects = function () {
        return Promise.resolve(mock_projects_1.PROJECTS);
    };
    ProjectService.prototype.create = function (name, url) {
        return this.http
            .post('http://52.52.67.116:3005/v1/rash/projects', JSON.stringify({ projectName: name, projectUrl: url }), { headers: this.headers })
            .toPromise()
            .then(function (res) { return res.json().data; })
            .catch(this.handleError);
    };
    ProjectService.prototype.handleError = function (error) {
        console.error('An error occurred', error); // for demo purposes only
        return Promise.reject(error.message || error);
    };
    return ProjectService;
}());
ProjectService = __decorate([
    core_1.Injectable()
], ProjectService);
exports.ProjectService = ProjectService;
//# sourceMappingURL=project.service.js.map
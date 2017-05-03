"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
var core_1 = require("@angular/core");
var Project_1 = require("./Project");
var project_service_1 = require("./project.service");
var ProjectFormComponent = (function () {
    function ProjectFormComponent(projectService) {
        this.projectService = projectService;
        this.model = new Project_1.Project(18, '', '', '', 2);
        this.submitted = false;
    }
    ProjectFormComponent.prototype.getProjects = function () {
        var _this = this;
        this.projectService.getProjects().then(function (projects) { return _this.projects = projects; });
    };
    ProjectFormComponent.prototype.onSubmit = function () {
        console.log(model);
        alert('hi');
        //this.projectService.create(model.name, model.gitUrl);
        console.log('hiii');
        this.getProjects();
        console.log('hiii');
        alert("hererere");
    };
    Object.defineProperty(ProjectFormComponent.prototype, "diagnostic", {
        // TODO: Remove this when we're done
        get: function () { return JSON.stringify(this.model); },
        enumerable: true,
        configurable: true
    });
    return ProjectFormComponent;
}());
ProjectFormComponent = __decorate([
    core_1.Component({
        selector: 'project-form',
        templateUrl: './project-form.component.html',
        providers: [project_service_1.ProjectService]
    }),
    __metadata("design:paramtypes", [project_service_1.ProjectService])
], ProjectFormComponent);
exports.ProjectFormComponent = ProjectFormComponent;
//# sourceMappingURL=project-form.component.js.map
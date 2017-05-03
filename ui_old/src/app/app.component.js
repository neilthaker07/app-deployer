"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var core_1 = require("@angular/core");
var AppComponent = (function () {
    function AppComponent() {
    }
    return AppComponent;
}());
AppComponent = __decorate([
    core_1.Component({
        selector: 'my-app',
        template: '<project-form><project-form>'
    })
], AppComponent);
exports.AppComponent = AppComponent;
var TableComponent = (function () {
    function TableComponent() {
    }
    return TableComponent;
}());
TableComponent = __decorate([
    core_1.Component({
        selector: 'my-app-table',
        template: '<project-table><project-table>'
    })
], TableComponent);
exports.TableComponent = TableComponent;
//# sourceMappingURL=app.component.js.map
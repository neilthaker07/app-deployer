import { Component } from '@angular/core';

import { Project }    from './Project';
import { ProjectService } from './project.service';

@Component({
  selector: 'project-form',
  templateUrl: './project-form.component.html',
   providers: [ProjectService]
})
export class ProjectFormComponent {
projects: Project[];
constructor(private projectService: ProjectService) { }

model = new Project(18, '', '', '',2);

getProjects(): void {
   this.projectService.getProjects().then(projects => this.projects = projects);
 }
  submitted = false;

  onSubmit() {
  console.log('hiii');

this.getProjects();
console.log('hiii');
alert("hererere");

   }

  // TODO: Remove this when we're done
  get diagnostic() { return JSON.stringify(this.model); }
}

import { Injectable } from '@angular/core';
import { PROJECTS } from './mock-projects';
import { Project } from './Project';

@Injectable()
export class ProjectService {

getProjects(): Promise<Project[]> {
return Promise.resolve(PROJECTS);

}
}

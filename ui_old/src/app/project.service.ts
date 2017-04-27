import { Injectable } from '@angular/core';
import { PROJECTS } from './mock-projects';
import { Project } from './Project';

@Injectable()
export class ProjectService {

private headers = new Headers({'Content-Type': 'application/json'});

getProjects(): Promise<Project[]> {
return Promise.resolve(PROJECTS);

}

create(name: string, url: string): Promise<Hero> {
    return this.http
      .post('http://52.52.67.116:3005/v1/rash/projects', JSON.stringify({projectName: name, projectUrl: url}), {headers: this.headers})
      .toPromise()
      .then(res => res.json().data as Hero)
      .catch(this.handleError);
  }
  private handleError(error: any): Promise<any> {
      console.error('An error occurred', error); // for demo purposes only
      return Promise.reject(error.message || error);
    }

}

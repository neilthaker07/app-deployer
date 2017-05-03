import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { HttpModule }    from '@angular/http';

import { AppComponent }  from './app.component';
import { TableComponent }  from './app.component';
import { ProjectFormComponent }  from './project-form.component';
import { ProjectTableComponent }  from './project-table.component';


@NgModule({
  imports:      [ BrowserModule , FormsModule, HttpModule],
  declarations: [ AppComponent, TableComponent, ProjectFormComponent, ProjectTableComponent],
  bootstrap:    [ AppComponent,TableComponent ]
})
export class AppModule { }

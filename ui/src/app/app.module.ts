import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';

import { AppComponent }  from './app.component';
import { ProjectFormComponent }  from './project-form.component';


@NgModule({
  imports:      [ BrowserModule , FormsModule],
  declarations: [ AppComponent,ProjectFormComponent ],
  bootstrap:    [ AppComponent ]
})
export class AppModule { }

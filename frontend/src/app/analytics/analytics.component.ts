import { Component, OnInit } from '@angular/core';
import { NgxChartsModule } from '@swimlane/ngx-charts';
@Component({
  selector: 'app-analytics',
  templateUrl: './analytics.component.html',
  styleUrls: ['./analytics.component.css']
})
export class AnalyticsComponent implements OnInit {
  view: any[] = [window.innerWidth , 400];
  data: any[];
  
  constructor() {
    this.data = [];
  }
  
  colorScheme = {
    domain: ['#5AA454'],
    text: ['#fff']
  };
  
  onSelect(event) {
    console.log(event);
    } 
  ngOnInit() {
  }

}

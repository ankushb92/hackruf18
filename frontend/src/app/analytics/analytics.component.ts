import { Component, OnInit, AfterViewInit } from '@angular/core';
import * as c3 from 'c3';

@Component({
  selector: 'app-analytics',
  templateUrl: './analytics.component.html',
  styleUrls: ['./analytics.component.css']
})
export class AnalyticsComponent implements OnInit, AfterViewInit {

  constructor() { }
    
  ngOnInit() {}

  ngAfterViewInit() {
    let chart = c3.generate({
    bindto: '#chart',
        data: {
            columns: [
                ['data1', 30, 200, 100, 400, 150, 250],
                ['data2', 50, 20, 10, 40, 15, 25]
            ]
        }
    });
}
}

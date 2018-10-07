import {Component, Input, OnInit} from '@angular/core';
import { NgxChartsModule } from '@swimlane/ngx-charts';
import {WellnessService} from "../wellness.service";
@Component({
  selector: 'app-analytics',
  templateUrl: './analytics.component.html',
  styleUrls: ['./analytics.component.css']
})
export class AnalyticsComponent implements OnInit {
  data: any[];
  @Input() session: string;
  constructor(public service: WellnessService) {

  }
  

  ngOnInit() {
    this.service.get_anal(this.session).subscribe((data)=>{console.log(data)})
  }



}

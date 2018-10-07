import {Component, Input, OnInit} from '@angular/core';
import { NgxChartsModule } from '@swimlane/ngx-charts';
import {WellnessService} from "../wellness.service";
@Component({
  selector: 'app-analytics',
  templateUrl: './analytics.component.html',
  styleUrls: ['./analytics.component.css']
})
export class AnalyticsComponent implements OnInit {
  data1: any[] = [];
  data2: any[] = [];
  @Input() session: string;
  constructor(public service: WellnessService) {

  }

  view: any[] = [700, 300];
  multi: any[];
  multi2: any[];
  // options
  showXAxis = false;
  showYAxis = true;
  gradient = false;
  showLegend = false;
  showXAxisLabel = true;
  xAxisLabel = 'Time';
  showYAxisLabel = true;
  yAxisLabel = '$';

  colorScheme = {
    domain: ['#69f0ae']
  };

  // line, area
  autoScale = true;



  ngOnInit() {
    this.view[0] = window.innerWidth - 30;
    this.service.get_anal(this.session).subscribe((data)=>{
      data['transaction'].forEach((e) => {
        this.data1.push({value: e['p'], name: e['tt']});

      });
      this.multi = [{name: 'hist', series:this.data1}];
        console.log(this.data1);

    });

    this.service.get_hold(this.session).subscribe((data)=>{
      data['holding'].forEach((e) => {
        this.data2.push({value: e['sum'], name: e['index']});

      });
      this.multi2 = [{name: 'hist', series:this.data2}];
      console.log(data);

    });
  }



}

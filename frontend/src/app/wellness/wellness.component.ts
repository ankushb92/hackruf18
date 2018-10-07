import { Component, OnInit } from '@angular/core';
import {WellnessService} from "./../wellness.service";

@Component({
    selector: 'app-wellness',
    templateUrl: './wellness.component.html',
    styleUrls: ['./wellness.component.css']
})

export class WellnessComponent implements OnInit {
    session: string = null;

    data: any = null;


  view: any[] = [window.innerWidth , 400];

  colorScheme = {
    domain: ['#5AA454'],
    text: ['#fff']
  };

  onSelect(event) {
    console.log(event);
  }
  constructor(public service: WellnessService) { }
    ngOnInit() {
        console.log("ONINIT");
        this.session = localStorage.getItem("session");
        this.service.get_wellness(this.session).subscribe((data) => {
            this.data = data;
            console.log(data);
        });
    }

}

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

    constructor(public service: WellnessService) { }
    ngOnInit() {
        console.log("ONINIT");
        this.session = localStorage.getItem("session");
        this.service.get_wellness(this.session).subscribe((data) => {
            this.data = data
        });
    }

}

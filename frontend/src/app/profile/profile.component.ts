import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import {ProfileService} from "../profile.service";


@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})

export class ProfileComponent implements OnInit {

  @Output() userChange: EventEmitter<object> = new EventEmitter<object>();
  constructor(public service: ProfileService) { }
  @Input() user: object;


  ngOnInit() {
    console.log(JSON.stringify(this.user));
  }

  updateUserProfile() {
    this.service.updateUser(this.user['name']['first'], this.user['name']['last'],
    this.user['age'], this.user['preferences']['currency'], this.user['preferences']['timeZone']).subscribe(
        (data) => {
            console.log(data);
        }
    )
  }
}

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
  @Input() session: string;

  ngOnInit() {
    if(this.user==null) this.user=JSON.parse(localStorage.getItem('user'));
  }

  updateUserProfile() {
    this.service.updateUserProfile(this.user, this.session).subscribe(
        (data) => {
            console.log(data);
            this.user=data;
            if(this.user['dob']!=null) {
              let date = new Date(this.user['dob']);
              this.user['dob'] = date;
            }
            console.log(this.user);
            this.userChange.emit(this.user);
            localStorage.setItem('user', JSON.stringify(data));
        }
    )
  }
}

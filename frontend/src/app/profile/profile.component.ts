import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import {ProfileService} from "../profile.service";
import {MatSnackBar} from "@angular/material";

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})

export class ProfileComponent implements OnInit {
  @Input() firstName: string;
  @Input() lastName: string;
  @Input() age: string;
  @Input() currency: string;
  @Input() timezone: string;
  @Input() userProfileChange: EventEmitter<string> = new EventEmitter<string>();
  constructor(public service: ProfileService, public snackBar: MatSnackBar) { }

  ngOnInit() {
  }

  updateUserProfile() {
    this.service.updateUser(this.first, this.last, this.age, this.currency, this.timezone).subscribe(
        (data) => {
            console.log(data);
        }
    )
  }
}

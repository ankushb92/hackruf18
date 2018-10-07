import {Component, OnInit} from '@angular/core';
import {LoginService} from "./login.service";
import {LogoutService} from "./logout.service";

@Component({
  selector: 'app',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  title = 'frontend';

  loggedIn: boolean = false;
  profile: boolean = false;
  userSession: string = null;

  user: object = null;

  constructor(public service: LogoutService) {}

  ngOnInit() {
    this.userSession = localStorage.getItem('session');
    this.user = JSON.parse(localStorage.getItem('user'));
    if( this.userSession != null) this.loggedIn=true;
  }

  logout(session: string) {
    this.service.logout(session).subscribe((data)=> {
      this.userSession=null;
      this.user=null;
      this.loggedIn = false;
      localStorage.removeItem('session');
      localStorage.removeItem('user');
    });
  }


  showProfile() {
    this.profile = true;
  }

  hideProfile() {
    this.profile = false;
  }

}

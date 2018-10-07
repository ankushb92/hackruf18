import {Component, OnInit, Input, Output, EventEmitter} from '@angular/core';
import {LoginService} from "../login.service";
import {MatSnackBar} from "@angular/material";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  @Input() userSession: string;
  @Input() loggedIn: boolean;
  @Input() user: object;
  @Output() userSessionChange: EventEmitter<string> = new EventEmitter<string>();
  @Output() loggedInChange: EventEmitter<boolean> = new EventEmitter<boolean>();
  @Input() userChange: EventEmitter<object> = new EventEmitter<object>();

  public username: string = "sbMemd7b5f5124626746c0765654ebe2c85048a1";
  public password: string = "sbMemd7b5f5124626746c0765654ebe2c85048a1#123";

  constructor(public service: LoginService, public snackBar: MatSnackBar) { }

  ngOnInit() {
  }

  login() {
    this.service.login(this.username, this.password).subscribe(
      (data) => {

        console.log(data);
        this.snackBar.open('Welcome ' + data['name']['first'] + ' ' + data['name']['last'], '', {duration: 3000} );
        this.userSession = data['session']['userSession'];
        this.loggedIn = true;
        localStorage.setItem('session', this.userSession);
        localStorage.setItem('user', JSON.stringify(data));
        this.userSessionChange.emit(this.userSession);
        this.loggedInChange.emit(this.loggedIn);
        this.userChange.emit(data);
        console.log(this.loggedIn);
      },
      (error) => {
        this.snackBar.open('Unsuccessful login', '', {duration: 3000} );
      }

    )
  }



}

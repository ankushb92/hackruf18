import { Component, OnInit, Input } from '@angular/core';
import {LoginService} from "../login.service";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  @Input() userSession: string;
  public username: string;
  public password: string;

  constructor(public service: LoginService) { }

  ngOnInit() {
  }

  login() {
    console.log(this.username);
    console.log(this.password);
    this.service.login(this.username, this.password).subscribe(
      (data) => console.log(data),
      (error) => console.log(error),
    )
  }

}

import { Injectable } from '@angular/core';
import { HttpRequest, HttpHandler, HttpEvent, HttpInterceptor } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';

@Injectable()
export class JwtInterceptor implements HttpInterceptor {
    intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
        // add authorization header with jwt token if available
        const currentUser = JSON.parse(localStorage.getItem('currentUser'));
        const token = JSON.parse(localStorage.getItem('token'));
        if (currentUser && token) {
            request = request.clone({
                setHeaders: {
                    Authorization: `JWT ${token}`
                }
            });
        }

        return next.handle(request);
    }
}

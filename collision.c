#include <stdio.h>
#include <string.h>
#include <openssl/evp.h>
// gcc collision.c - lcrypto - lssl

    int
    main(int argc, char *argv[])
{
    EVP_MD_CTX *mdctx;
    const EVP_MD *md;
    char mess1[] = "Test Message\n";
    char mess2[] = "Hello World\n";
    unsigned char md_value[EVP_MAX_MD_SIZE];
    // unsigned char md_value[3];
    unsigned int md_len=3, i;
    OpenSSL_add_all_algorithms();
    // if (argv[1] == NULL)
    // {
    //     printf("Usage: mdtest digestname\n");
    //     exit(1);
    // }

    // md = EVP_get_digestbyname(argv[1]);
    // hash value of 24 bits, 3 bytes -> letters
    // 
    md = EVP_get_digestbyname(OBJ_nid2sn(65)); // hash rsa
    if (md == NULL)
    {
        printf("Unknown message digest %s\n", argv[1]);
        exit(1);
    }

    mdctx = EVP_MD_CTX_create(); // allocates and returns a digest context
    EVP_DigestInit_ex(mdctx, md, NULL); // sets up digest context ctx to use a digest type, supplied by a fucntion such as EVP_sha1(), if null then default implementation of digest type
    EVP_DigestUpdate(mdctx, mess1, strlen(mess1)); // hashes cnt bytes of data at d into the digest context ctx
    EVP_DigestUpdate(mdctx, mess2, strlen(mess2));
    
    EVP_DigestFinal_ex(mdctx, md_value, &md_len); // gets digest value from ctx and places in md, 
    EVP_MD_CTX_destroy(mdctx);

    printf("Digest is: ");
    printf("%d\n", md_len);
    for (i = 0; i < md_len; i++)
        printf("%02x", md_value[i]); //my values is hash array
    printf("\n");
    EVP_cleanup();

    exit(0);
}
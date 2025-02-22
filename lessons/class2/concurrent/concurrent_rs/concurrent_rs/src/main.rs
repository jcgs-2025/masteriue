use std::time::Instant;
 
use anyhow::{Ok, Result};
use futures::future::join_all;
 
async fn download_page(url: &str) -> Result<String> {
    let response = reqwest::get(url).await?;
    let content = response.bytes().await?;
    Ok(format!("{} - {} bytes", url, content.len()))
}
 
#[tokio::main]
async fn main() -> Result<()> {
    let urls = vec![
        "https://www.python.org",
        "https://www.github.com",
        "https://www.google.com",
    ];
 
    let start = Instant::now();
 
    let mut futures = vec![];
    for url in urls {
        futures.push(tokio::spawn(download_page(url)));
    }
 
    let results = join_all(futures).await;
 
    for result in results {
        let out = result.unwrap().unwrap();
        println!("{}", out);
    }
 
    println!("Downloaded all pages in {:?}", start.elapsed());
 
    Ok(())
}
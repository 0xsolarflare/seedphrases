use bip39::{Mnemonic, Language};

fn main() {
    // Get the BIP39 word list
    let word_list = Language::English.word_list();
    
    // println!("Word List:");
    // for word in word_list {
    //     println!("{}", word);
    // }
    
    for &word in word_list {
        // Construct a 12-word mnemonic with the same word repeated
        let phrase = vec![word; 12].join(" ");
        
        // Check if the phrase is a valid BIP39 mnemonic
        if Mnemonic::parse(&phrase).is_ok() {
            println!("{}", phrase);
        }
    }
}

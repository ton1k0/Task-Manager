import {IconButton} from "@chakra-ui/react";
import {BsChat} from "react-icons/bs";

export function ChatIcon() {
    return(
        <IconButton
            _hover={{
                background: "white",
            }}
            colorScheme='purple'
            aria-label='AiOutlineHome2'
            height='50px'
            width='50px'
            variant='ghost'
            icon={<BsChat/>}>
        </IconButton>
    )
}
import {IconButton} from "@chakra-ui/react";
import {BsBoxArrowRight} from "react-icons/bs";

export function ExitIcon() {
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
            icon={<BsBoxArrowRight/>}>
        </IconButton>
    )
}
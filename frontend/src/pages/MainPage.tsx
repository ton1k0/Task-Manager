import {Avatar, Badge, Flex, IconButton, Image, Box, Text} from "@chakra-ui/react";
import {AiOutlineHome} from "react-icons/ai";
import {BsChat, BsBell, BsGear, BsBoxArrowRight} from "react-icons/bs";

function MainPage() {
    return (
        <Flex>
            <Flex borderRadius='20' bg='gray.100' p={2} minHeight='calc(100vh - 32px)' justifyContent='space-between'
                  minWidth='max-content' maxWidth='40px' flexDirection='column' alignItems='center' marginLeft='2'
                  marginY='4'>
                <Flex flexDirection='column' gap='4' alignItems='center'>
                    <Avatar size='md' borderRadius='20%' name='Dan Abrahmov' src='https://bit.ly/dan-abramov'/>
                    <IconButton
                        _hover={{
                            background: "white",
                        }}
                        colorScheme='purple'
                        aria-label='AiOutlineHome'
                        height='50px'
                        width='50px'
                        variant='ghost'
                        icon={<AiOutlineHome/>}>
                    </IconButton>
                    <IconButton
                        _hover={{
                            background: "white",
                        }}
                        colorScheme='purple'
                        aria-label='AiOutlineHome2'
                        height='50px'
                        width='50px'
                        variant='ghost'
                        icon={<BsBell/>}>
                    </IconButton>
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
                </Flex>
                <Flex flexDirection='column' gap='4'>
                    <IconButton
                        _hover={{
                            background: "white",
                        }}
                        colorScheme='purple'
                        aria-label='AiOutlineHome2'
                        height='50px'
                        width='50px'
                        variant='ghost'
                        icon={<BsGear/>}>
                    </IconButton>
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
                </Flex>
            </Flex>
            <Flex marginLeft='5' marginY='4'>
                <Box maxW='sm' maxH='sm' borderWidth='1px' borderRadius='lg' overflow='hidden'>
                    <Text>Project efficiency</Text>
                </Box>
            </Flex>
        </Flex>
    );
}

export default MainPage;

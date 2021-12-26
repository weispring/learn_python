/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50720
Source Host           : localhost:3306
Source Database       : learn

Target Server Type    : MYSQL
Target Server Version : 50720
File Encoding         : 65001

Date: 2021-12-26 21:12:49
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for t_love_articles
-- ----------------------------
DROP TABLE IF EXISTS `t_love_articles`;
CREATE TABLE `t_love_articles` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `author` varchar(30) DEFAULT NULL,
  `content` varchar(500) DEFAULT NULL,
  `bookName` varchar(50) DEFAULT NULL,
  `commentNum` int(11) DEFAULT NULL,
  `loveNum` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=114 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_love_articles
-- ----------------------------
INSERT INTO `t_love_articles` VALUES ('1', '刘希夷', '年年岁岁花相似，岁岁年年人不同', '《相和歌辞·白头吟》', '4', '0');
INSERT INTO `t_love_articles` VALUES ('2', '李宫俊', '如果有好感，那就是喜欢，如果这种好感经得起考验，那就是爱。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('3', '李宫俊', '李宫俊说：和别人谈起你,是我想你的方式。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('4', '李宫俊', '保持一颗淡然的心不卑不亢心中放下眼前一切不骄不燥对我态度好与不好不喜不悲突然离我而去的人不闻不问当困难摆在我面前不屈不挠 . 不慌不忙. 这是我的向往', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('5', '李宫俊', '有人说：越炫耀什么，越缺少什么。但我却以为：越缺少什么，越觉得别人炫耀什么。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('6', '李宫俊', '上联：尝遍天下美食下联：赏完世间何物 上联：尝遍天下美食下联：读尽人间风尘 上联：尝遍天下美食下联：看尽人间秀色', '《李宫俊的诗》', '1', '0');
INSERT INTO `t_love_articles` VALUES ('7', '李宫俊', '我们都很好，只是时间不凑巧。', '《李宫俊的诗》', '4', '0');
INSERT INTO `t_love_articles` VALUES ('8', '李宫俊', '李宫俊说：我假装无所谓，却发现你是真的不在乎。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('9', '李宫俊', '我是一个不喜欢等待的人，买东西我只想要现货。 ​​​', '《李宫俊的诗》', '1', '0');
INSERT INTO `t_love_articles` VALUES ('10', '李宫俊', '今天我看到一个人，背影很像你，然后我看了好久。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('11', '李宫俊', '不开心的时候请假装乐观,装着装着可能就像了。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('12', '李宫俊', '李宫俊说：若不身在其中，何来感同身受。', '《李宫俊的诗》', '1', '0');
INSERT INTO `t_love_articles` VALUES ('13', '李宫俊', '李宫俊说：我假装没有看你，你也假装欣赏风景。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('14', '李宫俊', '我不联系你，只是不想让自己觉得自己很多余。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('15', '李宫俊', '从陌生人变回陌生人, 那就是我们的故事。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('16', '李宫俊', '我什么都没有，只有，一个不确定的明天，一个不知道的未来。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('17', '李宫俊', '我怕永不再见，我也怕再次重逢。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('18', '李宫俊', '我将句子写给你，打动的却是我自己。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('19', '李宫俊', '李宫俊说：我记得你爱我，或许是我记反了。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('20', '李宫俊', '李宫俊说：你是我的可遇不可求，可遇不可留，可遇不可有。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('21', '李宫俊', '不要试图挽留一个要走的人，你用什么挽留她，她就会带走什么。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('22', '李宫俊', '李宫俊说：我假装无所谓，却发现你是真的不在乎。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('23', '李宫俊', '车站有两个地方最感人：一个入口，一个出口。一个是不想让你走，一个是等你回来。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('24', '李宫俊', '人成熟到一定程度，大概是可怜的，连精神崩溃都是体面的、可控的、点到为止的。 一转身又能变成那个稳重的，张弛有度，滴水不漏的人。 ​​​', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('25', '李宫俊', '记忆不复成殇，回忆终成绝想。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('26', '李宫俊', '等待，并非执拗。只是我也很好奇，想看一下，我是有多喜欢你。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('27', '李宫俊', '你曾经喜欢我，现在不喜欢了，那是我没本事，我不怪你。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('28', '李宫俊', '李宫俊说：和别人谈起你,是我想你的方式。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('29', '李宫俊', '我听说,一次原谅,会换来,两次背叛。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('30', '李宫俊', '年轻真好啊，年轻才敢把自己置身于狼狈和危险中。 ​​​', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('31', '李宫俊', '自知平庸，还在挣扎。 ​​​', '《李宫俊的诗》', '1', '0');
INSERT INTO `t_love_articles` VALUES ('32', '李宫俊', '“头等舱可以优先登机 银行VIP可以不用排队 演唱会最贵的票位置也最好 世界从不平等”', '《李宫俊的诗》', '2', '0');
INSERT INTO `t_love_articles` VALUES ('33', '李宫俊', '有的时候， 一个APP的消失叛逃，不在于它在你的手机存在了几年，反复翻了多少次。仅仅只是，几周不能打开而被卸载。选择另外一个相似的APP安装。尽管页面很不习惯。', '《李宫俊的诗》', '2', '0');
INSERT INTO `t_love_articles` VALUES ('34', '李宫俊', '我说着清醒的疯话，做着理智的荒唐事。喜欢去无果的付出，期待着暗淡的未来。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('35', '李宫俊', '其实，那些从不给你承诺的人，为你做了更多。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('36', '李宫俊', '没有与生俱来的情商，全都是准备好的智商。 ​​​', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('37', '李宫俊', '我这十年生活的城市分别为，淄博、青岛、连云港、曲阜，很奇怪，我对这四个城市都不熟悉，也都无归属感，对我来说，大致在哪里生活都是一样的。 ​​​', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('38', '李宫俊', '普通人的情绪一点都不值钱。 ​​​', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('39', '李宫俊', '明明在喜欢你之前过的很好。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('40', '李宫俊', '一开始以为是你错了，然后我觉得是我错了，后来觉得是我们全错了，不，其实我们都没错。 ​​​', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('41', '李宫俊', '一道古城墙，一条老街，一座老屋，一卷老照片，一首旧情歌，一句曾经丰满的语言。斑驳的历史，厚重的情感，或潇洒，或凄美，或黯然，或叹息，或怅然・・・・・・', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('42', '李宫俊', '不会频繁地更新文字，却习惯性地在临睡前点开这个网站，看看我喜欢的人们写下的文字，默默观望他们的喜怒哀乐，在他们的思想中穿梭流动，予以祝福。发现，有些朋友已经如我一般渐渐隐去了，可还是保留着太多的不舍和眷恋。是啊。这片虚幻的空中花园，开满了喜悦和悲伤的花朵，每个人都是用心血浇灌的。', '《李宫俊的诗》', '1', '0');
INSERT INTO `t_love_articles` VALUES ('43', '李宫俊', '当目标的实现超过了自身的实力这时候就需要许愿了。 ​​​', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('44', '李宫俊', '无论多么不情愿承认，大侄女终归不是你的大侄女了。那天乃至随后的某些日子，亚当贪婪的想要吞咽的那颗青涩果子，不也慢慢成熟了吗？它会越来越诱人，但还好又开始有一条忠诚的蛇守着她了。那就这样吧，英雄们前赴后继，往来如风，唯深渊凝视星辰，恒古未变。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('45', '李宫俊', '物是人非，人均四年。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('46', '李宫俊', '我给你一个机会，向我表白。如果你不好好把握，我再给你一个。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('47', '李宫俊', '求个明白人，问条不归路。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('48', '李宫俊', '不要对我好，我习惯了，会期待更多。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('49', '李宫俊', '什么都不知道，什么都想知道。 ​​', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('50', '李宫俊', '花落人不在, 人散花不知。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('51', '李宫俊', '两相忘，从来未忘。两相望，别来无恙。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('52', '李宫俊', '你去了另一个城市，我也可以安心了，不用想着会不会再偶遇。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('53', '李宫俊', '马上要踏入十二月，日历薄得可怜，薄得让人感觉悲壮。 ​​​', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('54', '李宫俊', '如果有人告诉你他很喜欢一首歌，那首歌的歌词是给你的。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('55', '李宫俊', '命运给你一个考验，一定是因为它想给你某样东西。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('56', '李宫俊', '不去刻意的追求随性，基本就能做到随性了。 ​​​', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('57', '李宫俊', '世间聚散离合自有定数，但定数如何要看你自己。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('58', '李宫俊', '上帝为你关上一扇门的同时,也一定会为你加把锁。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('59', '李宫俊', '未来对我来说远没有过去重要，我是面向过去而活的人，从来不是面向未来而活的人。 ​​​', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('60', '李宫俊', '有些人，终究做朋友就好。因为退一步舍不得，进一步又没资格。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('61', '李宫俊', '男孩子，你是这三步成长，抑或倒退。 最初，许诺一生，志意满满。然后，不言一生，因为明白不会有一生。最终，矫作一生，纵使明知不会有一生。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('62', '李宫俊', '谢谢陌生又熟悉的你们。我了解你们的文字，熟悉你们的语言风格，并或多或少地从你们各自的字里行间窥视到一些各自的脾气性情。基于此，喜欢上了你们这些朋友。当然，这些欢喜是默默在心河流淌的。默不作声，潺潺流过。愿你们一切都好。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('63', '李宫俊', '你不能说因为某个名人/某个伟人说过什么什么，你就认为，并且要求我也认为这句话是对的。每个人的人生观与价值观都不尽相同，没有谁的言论与行为是放之天下皆准的。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('64', '李宫俊', '人生不知足，何来的幸福。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('65', '李宫俊', '时间笑我不成长，我笑时间太猖狂。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('66', '李宫俊', '有些人，只适合好奇，不适合在一起。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('67', '李宫俊', '自与你错过之后，爱上的都是朋友。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('68', '李宫俊', '厌恶情绪严重，想自闭，不想和社会接轨。 ​​​', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('69', '李宫俊', '在所有的哺乳类动物中只有人类会干傻事。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('70', '李宫俊', '所有未曾燃尽的梦想都变成了不可燃垃圾。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('71', '李宫俊', '我明明是一个十分任性的人,却时常觉得自己过的委屈。 ​​​', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('72', '李宫俊', '生活就是提着桶狗血作画。 ​​​', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('73', '李宫俊', '每一个失眠的夜晚，我都试图总结过去这半生。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('74', '李宫俊', '我以为我会忘了你，我以为你会记得我。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('75', '李宫俊', '人想要开心还是要努力实现自己的内循环。 ​​', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('76', '李宫俊', '朋友问了我四遍同样的问题，我的四次回答都不一样。 ​​​', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('77', '李宫俊', '大抵无论事业或恋爱，从外面看上去，就自带了美好滤镜的加工吧。别人的日子看上去总是更容易过些。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('78', '李宫俊', '接完今年最后一个电话，才可以说我的今年就这么过去了，没有发生什么坏事，完全无话可说，这无疑是我人生中很好的一年。 ​​​​', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('79', '李宫俊', '人啊，经历了，就是容易热泪盈眶。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('80', '李宫俊', '不想让别人看到你微笑的样子，我不想因此多个情敌。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('81', '李宫俊', '做回自己，总有人会爱上你的全部。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('82', '李宫俊', '对不起，是我情不自禁。我忘了，我只是一个过客。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('83', '李宫俊', '不是所有的悲伤，都能用文字诠释。而是所有悲伤，都能从文字中得到安慰。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('84', '李宫俊', '其实我爱你的意思是——我想被你爱。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('85', '李宫俊', '不联络不代表不想念，而是想念了又能如何?', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('86', '李宫俊', '当失望超过期望时, 我便会变得冷漠无情。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('87', '李宫俊', '早知适可而止，不会落得如此。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('88', '李宫俊', '一个人其实也很好;不过是寂寞时没人拥抱;不过是孤单时没人依靠。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('89', '李宫俊', '当目标的实现超过了自身的实力这时候就需要许愿了。 ​​​', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('90', '李宫俊', '我表白，你拒绝。我连续表白，你连续拒绝。我们好有默契。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('91', '李宫俊', '我放开了，但还没放下。我恢复了，但还没痊愈。我想开了，但还有怀念。我忘记了，但还有回忆。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('92', '李宫俊', '从此忘了你，晚安我自己。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('93', '李宫俊', '假装自己和成年人是同类人这种事情我到现在都不愿意做。 ​​​', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('94', '李宫俊', '争强好胜，只会让自己成为孤家寡人；', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('95', '李宫俊', '我很容易原谅人，但是我很记仇：原谅不代表我忘记。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('96', '李宫俊', '开心果并不能令人开心，但是酒对很多人都有效。人类起名起错了，应该把酒这种东西改名叫做“开心果”。 ​​​', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('97', '李宫俊', '十年以前，我觉得喜欢喝酒是上不了台面的追求，觉得有向往的人不应该将烦恼沉溺于酒精的麻痹。十年之后，我成了一个独自喝酒，不求质量，只求迅速上头的人。 ​​​', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('98', '李宫俊', '后来亲自经历过了才明白，有些人的恶意其实是顺水推舟的。他们不辨真假，不论对错，只是为了逞一时口舌之快来获得些许快感。他们甚至根本不知道自己所言所行会给别人带去怎样的伤害。 ​​​', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('99', '李宫俊', '节俭是因为无能，想到花掉的钱怎么努力都赚不回来，就只能努力省钱。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('100', '李宫俊', '薄情过，我也深情过，求不得的，也是我。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('101', '李宫俊', '人见人穷绕着走，狗见家穷死也守！落叶时分而知秋，受穷之后而知愁！', '《李宫俊的诗》', '1', '0');
INSERT INTO `t_love_articles` VALUES ('102', '李宫俊', '你握住了那就是你的。你握不住就别怪别人抢了他。早安！', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('103', '李宫俊', '在爱情面前，我们有时会变得盲目，但不能失去自我而变得卑微…', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('104', '李宫俊', '陈泽凯给我转3700！ 我', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('105', '李宫俊', '有些人,到此为止；有些事, 由不得你。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('106', '李宫俊', '如果你不懂我内伤，就别识破我伪装。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('107', '李宫俊', '我曾为你敲冰求火，你可曾记得我？', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('108', '李宫俊', '如果按时付费的话，我想很多人还可以爱你久一点。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('109', '李宫俊', '少女心微溶于水。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('110', '李宫俊', '世间多是，把所有鸡蛋放在一个篮子里的焦虑。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('111', '李宫俊', '憧憬不屈不挠，期待余烬燃烧。', '《李宫俊的诗》', '0', '0');
INSERT INTO `t_love_articles` VALUES ('112', '李宫俊', '假如有一天，你不慎误入迷途，失足掉入河中，请记得有一条河叫做重生。', '《李宫俊的诗》', '1', '0');
INSERT INTO `t_love_articles` VALUES ('113', '李宫俊', '时间真快啊，我上次跟人聊天，被人拿着拖鞋揍已经大约是三年前的事了... ​​​​', '《李宫俊的诗》', '0', '0');
